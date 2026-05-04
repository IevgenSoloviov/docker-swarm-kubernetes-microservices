#!/bin/bash

LOG="/var/log/suricata/eve.json"
EMAIL="admin@example.com"
STATE_DIR="/var/lib/suricata-alert"
COOLDOWN=300
BAN_TIME=600
BLOCK_LOG="/var/log/suricata-active-response.log"
CHAIN="SURICATA_BLOCK"

mkdir -p "$STATE_DIR"
touch "$BLOCK_LOG"

tail -Fn0 "$LOG" | while read -r line; do

    echo "$line" | grep '"event_type":"alert"' >/dev/null || continue

    SIGNATURE=$(echo "$line" | grep -oP '"signature":"\K[^"]+')
    SRC_IP=$(echo "$line" | grep -oP '"src_ip":"\K[^"]+')
    DEST_IP=$(echo "$line" | grep -oP '"dest_ip":"\K[^"]+')
    TIME=$(echo "$line" | grep -oP '"timestamp":"\K[^"]+')

    case "$SIGNATURE" in
        "Possible brute force SSH"|"Possible escaneig de ports"|"Acces a serveis Docker Infraestructura Ansible"|"SCAN detectat contra infraestructura"|"SCAN sortint des de LAN")
            ;;
        *)
            continue
            ;;
    esac

    SAFE_NAME=$(echo "$SIGNATURE" | tr ' /' '__' | tr -cd '[:alnum:]_-')
    STATE_FILE="$STATE_DIR/$SAFE_NAME.last"

    NOW=$(date +%s)

    if [ -f "$STATE_FILE" ]; then
        LAST_SENT=$(cat "$STATE_FILE" 2>/dev/null)
    else
        LAST_SENT=0
    fi

    ELAPSED=$((NOW - LAST_SENT))
    ACTION_MSG="Sense resposta automàtica."

    # Bloqueig immediat independent del cooldown
    if [ "$SIGNATURE" = "Possible brute force SSH" ]; then
        if ! iptables -C "$CHAIN" -s "$SRC_IP" -j DROP 2>/dev/null; then
            iptables -A "$CHAIN" -s "$SRC_IP" -j DROP
            echo "$(date '+%F %T') - IP $SRC_IP bloquejada temporalment durant $BAN_TIME segons" >> "$BLOCK_LOG"
            ACTION_MSG="IP atacant bloquejada temporalment durant $BAN_TIME segons."

            (
                sleep "$BAN_TIME"
                iptables -D "$CHAIN" -s "$SRC_IP" -j DROP 2>/dev/null
                echo "$(date '+%F %T') - IP $SRC_IP desbloquejada automàticament" >> "$BLOCK_LOG"
            ) &
        else
            ACTION_MSG="La IP atacant ja estava bloquejada temporalment."
        fi
    fi

    # Correu subjecte a cooldown
    if [ "$ELAPSED" -ge "$COOLDOWN" ]; then
        {
            echo "Alerta IDS detectada"
            echo
            echo "Hora: $TIME"
            echo "IP origen: $SRC_IP"
            echo "IP destí: $DEST_IP"
            echo "Signatura: $SIGNATURE"
            echo
            echo "Acció: $ACTION_MSG"
            echo
            echo "Revisa el dashboard de Kibana per més informació."
        } | mail -s "ALERTA IDS - $SIGNATURE" "$EMAIL"

        echo "$NOW" > "$STATE_FILE"
    fi

done

