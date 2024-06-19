# Webstack Monitoring

This project involves setting up and configuring monitors in Datadog to track read and write requests per second on a web server. The monitors will help in determining the system's performance and scalability requirements.

## Monitors Setup

### Monitor for Read Requests per Second
1. Navigate to **Monitors > New Monitor**.
2. Choose **Metric** for the monitor type.
3. Search for `system.io.r_s` and select it.
4. Define alert conditions and notification settings.
5. Save the monitor with an appropriate name.

### Monitor for Write Requests per Second
1. Navigate to **Monitors > New Monitor**.
2. Choose **Metric** for the monitor type.
3. Search for `system.io.w_s` and select it.
4. Define alert conditions and notification settings.
5. Save the monitor with an appropriate name.

### Verification
1. Check the monitors under **Monitors > Manage Monitors**.
2. Ensure they are active and correctly configured.

## Bash Scripts

### Script to Check Datadog Agent Status
This script checks if the Datadog agent is running on the server.

```bash
#!/usr/bin/env bash
# This script checks if the Datadog agent is running

if systemctl is-active --quiet datadog-agent; then
    echo "Datadog agent is running"
else
    echo "Datadog agent is not running"
fi
