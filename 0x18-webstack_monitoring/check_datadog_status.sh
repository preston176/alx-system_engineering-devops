#!/usr/bin/env bash
# This script checks if the Datadog agent is running

if systemctl is-active --quiet datadog-agent; then
    echo "Datadog agent is running"
else
    echo "Datadog agent is not running"
fi
