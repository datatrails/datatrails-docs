---
title: "Compliance API"
description: "Compliance API Reference"
lead: "Compliance API Reference"
date: 2021-06-09T12:07:13+01:00
lastmod: 2021-06-09T12:07:13+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 106
toc: true
---

## Compliance API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Types of Compliance Policies

Compliance Posture is measured against user-defined rule sets called Compliance Policies.

Compliance policies are created once and then Assets can be tested against them at any point in time. 

For instance, a policy might state that “Maintenance Alarm Events must be answered with a Maintenance Report Event recorded in 72 hours”. 

This creates a Compliance Policy object in the system against which any asset can be tested as needed.

RKVST allows users to define Compliance Policies of the following types:

#### COMPLIANCE_SINCE

This Compliance Policy checks if the time since the last occurence of a specific Event Type has elapsed a specified threshold. 

For example “Time since last Maintenance must be less than 72 hours”:

```json
{
    "compliance_type": "COMPLIANCE_SINCE",
    "description": "Maintenance should be performed every 72h",
    "display_name": "Regular Maintenance",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ]
    "event_display_type": "Maintenance Performed",
    "time_period_seconds": "259200"
}
```

{{< table >}}
| Attribute | Description |
|-----------|-------------|
| `event_display_type` | Type of event we want to check with this compliance policy |
| `time_period_seconds` | The maximum amount of time allowed since a specified event type last occurred in seconds |
{{< /table >}}

#### COMPLIANCE_CURRENT_OUTSTANDING

This Compliance Policy will only pass if there is an associated answering event addressing a specified outstanding event.

To correlate events define the attribute `arc_correlation_id` in the Event Attributes and set it to the same value on each pair of events that are to be associated. 

For example defining pairs of Events like `Maintenance Request` and `Maintenance Performed`: 

```json
{
    "compliance_type": "COMPLIANCE_CURRENT_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests",
    "display_name": "Outstanding Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ]
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type":  "Maintenance Performed"
}
```

{{< table >}}
| Attribute | Description |
|-----------|-------------|
| `event_display_type` | Type of event that should be addressed by the event defined in `closing_event_display_type` |
| `closing_event_display_type` | Type of event addressing the event defined in `event_display_type` |
{{< /table >}}

#### COMPLIANCE_PERIOD_OUTSTANDING

This Compliance Policy will only pass if the time between a pair of correlated events did not exceed the defined threshold. 

To correlate events define the attribute `arc_correlation_id` in the Event Attributes and set it to the same value on each pair of events that are to be associated. 

For example, a policy checking that the time between `Maintenance Request` and `Maintenance Performed` Events does not exceed the maximum 72 hours:
```json
{
    "compliance_type": "COMPLIANCE_PERIOD_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests",
    "display_name": "Outstanding Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ]
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type":  "Maintenance Performed",
    "time_period_seconds": "259200"
}
```

{{< table >}}
| Attribute | Description |
|-----------|-------------|
| `event_display_type` | Type of event that should be addressed by the event defined in `closing_event_display_type` |
| `closing_event_display_type` | Type of event addressing the event defined in `event_display_type` |
| `time_period_seconds` | Maximum amount of time that can elapse between associated events in seconds |
{{< /table >}}

#### COMPLIANCE_DYNAMIC_TOLERANCE

This Compliance Policy will only pass if the time between a pair of correlated events did not exceed the defined variability. 

To correlate events define the attribute `arc_correlation_id` in the Event Attributes and set it to the same value on each pair of events that are to be associated. 

For example, a policy checking that the time between `Maintenance Request` and `Maintenance Performed` Events in the last week does not exceed a variability of 0.5 standard deviations around the mean:

```json
{
    "compliance_type": "COMPLIANCE_DYNAMIC_TOLERANCE",
    "description": "Average time between Maintenance Requested/Performed"
    "display_name": "outlying Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ]
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type": "Maintenance Performed",
    "dynamic_window": 604800,
    "dynamic_variability": 0.5
}
```

{{< table >}}
| Attribute | Description |
|-----------|-------------|
| `event_display_type` | Type of event that should be addressed by the event defined in `closing_event_display_type` |
| `closing_event_display_type` | Type of event addressing the event defined in `event_display_type` |
| `dynamic_window` | Number of seconds in the past - only events in this time window are considered. |
| `dynamic_variability` | Exceeding this number of standard deviations from the mean will cause compliance to fail for a particular pair of matching events. |
{{< /table >}}

#### COMPLIANCE_RICHNESS

This Compliance Policy will only pass if the assertions conducted on an attribute value pass. 

An assertion is comprised of: an attribute name, a comparison value and an operator to compare with; for example `rad<7`. 

The operator can be one of six relational operators: equal to, not equal to, greater than, less than, greater than or equal to, less than or equal to; `[=|!=|>|<|>=|<=]`.

Assertions are comprised of two lists, an inner list and outer list. The inner list states that, if any of the assertions pass, then the list is compliant (`OR` logic). For example: 

```json
{“or”: [“rad<7”, “rad=10”]}. 
```

The outer list states that, all inner lists need to be compliant in order for the policy to be compliant (`AND` logic).

Compliance is a signal, not a perfect answer. Therefore equivilence of floats is exact, not approximate.

```json
{
    "compliance_type": "COMPLIANCE_RICHNESS",
    "description": "Rad level is less than 7"
    "display_name": "Rad limit",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ],
    "richness_assertions": [
        { "or": ["rad<7"]}
    ],
}
```

{{< table >}}
| Attribute | Description |
|-----------|-------------|
| `richness_assertions`| The assertions to be made, against asset attributes, to check if the asset is compliant. |
{{< /table >}}

### Compliance Policy Creation

Create a Policy with:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```

Using data from `/path/to/jsonfile` in the format described in [Types of Compliance Policies](./types-of-compliance-policies).

Sample response:

```json
{
    "identity": "compliance_policies/6a951b62-0a26-4c22-a886-1082297b063b",
    "compliance_type": "COMPLIANCE_CURRENT_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests",
    "display_name": "Outstanding Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/5eef2b71-35c1-4376-a166-6c64bfa72f4b"]}
    ]
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type":  "Maintenance Performed",
    "time_period_seconds": "259200"
}
```

### Checking Compliance

The compliancev1 endpoint reports on the status of an Asset’s Compliance with Compliance Policies.

Query the endpoint:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v1/compliance/assets/6a951b62-0a26-4c22-a886-1082297b063b
```

or if determining compliance at some historical date:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v1/compliance/assets/6a951b62-0a26-4c22-a886-1082297b063b?compliant_at=2019-11-27T14:44:19Z
```
The response is:

```json
{
    "compliant": true,
    "compliance": [
        {
            "compliance_policy_identity": "compliance_policies/0000-0000-000000000-00000000",
            "compliant": true,
            "reason": ""
        }
    ],
    "compliant_at": "2019-11-27T14:44:19Z"
}
```

## Compliance OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/compliancev1.swagger.json" >}}