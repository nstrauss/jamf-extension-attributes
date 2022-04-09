#!/bin/zsh

# Loop through all wireless network interfaces and check if a proxy bypass is set

# Set internal field separator to new line
IFS=$'\n'

# Initialize array
bypass_domains=()

# Loops through the list of network services
for service in $(networksetup -listallnetworkservices | tail +2); do
    # Get proxy URL for each relevant network service
    if [[ "$service" =~ "Wi-Fi" ]]; then
        domains=$(/usr/sbin/networksetup -getproxybypassdomains "$service")
        for dom in $domains; do
            if [[ "$dom" != *"any bypass domains"* ]]; then
                bypass_domains+=("$dom")
            fi
        done
    fi
done

# Find unique entries and format
sorted_domains=($(printf "%s\n" "${bypass_domains[@]}" | sort -u | tr '\n' ' ' | sed -e 's/[[:space:]]*$//'))

# Evaluate array. Check if any bypass domains were set
if [[ ${#bypass_domains[@]} -gt 0 ]]; then
    echo "<result>$sorted_domains</result>"
else
    echo "<result>None</result>"
fi

unset IFS
