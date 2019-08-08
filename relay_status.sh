#!/bin/zsh 

# Finds running process components of Lightspeed Relay Smart Agent
# If running returns mobilefilter version
# If not running looks to see all components are installed
# If installed, but without a process running returns "Installed with Errors"
# If not installed returns "Not Installed"

if pgrep -x proxyforce >/dev/null 2>&1 \
    && pgrep -x smartagentjs >/dev/null 2>&1 \
    && pgrep -x lsproxy >/dev/null 2>&1 \
    && pgrep -x mobilefilter >/dev/null 2>&1; then
    
    printf "<result>$(/usr/local/bin/mobilefilter -v)</result>"
elif
    ls /usr/local/bin/proxyforce >/dev/null 2>&1 \
    && ls /usr/local/bin/smartagentjs >/dev/null 2>&1 \
    && ls /usr/local/bin/lsproxy >/dev/null 2>&1 \
    && ls /usr/local/bin/mobilefilter >/dev/null 2>&1; then

    printf "<result>Installed with Errors</result>"
else
    printf "<result>Not Installed</result>"
fi

