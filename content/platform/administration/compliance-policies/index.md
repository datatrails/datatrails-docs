---
 title: "Compliance Policies"
 description: "Creating and Managing Compliance Policies"
 lead: "Creating and Managing Compliance Policies"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   platform:
     parent: "administration"
 weight: 45
 toc: true
---

## Creating a Compliance Policy

Compliance Policies are user-defined rule sets that Assets can be tested against. Compliance Policies only need to be created once; all applicable Assets will be tested against that policy thereafter. 

For example, a policy might assert that “Maintenance Alarm Events must be addressed by a Maintenance Report Event, recorded within 72 hours of the alarm”. This creates a Compliance Policy in the system which any Asset can be tested against as needed.

{{< note >}}
**Note:** Creation and editing of Compliance Policies is only supported through the API.
{{< /note >}}

RKVST allows for several types of Compliance Policies: 

1. ***COMPLIANCE_SINCE:*** checks the time elapsed since a specific type of Event has not exceeded set threshold. 

For example, "time since last maintenance must be less than 72 hours".

{{< tabs name="compliance_since" >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_SINCE policy
      print_response: true
    description: Maintenance should be performed every 72h
    display_name: Regular Maintenance
    compliance_type: COMPLIANCE_SINCE
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Performed
    time_period_seconds: "259200"
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_SINCE",
    "description": "Maintenance should be performed every 72h",
    "display_name": "Regular Maintenance",
    "asset_filter": [
        { "or": ["attributes.arc_home_location_identity=locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Performed",
    "time_period_seconds": "259200"
}
```
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```
{{< /tab >}}}
{{< /tabs >}}

2. ***COMPLIANCE_CURRENT_OUTSTANDING:*** checks if there is a closing Event addressing an outstanding Event.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of Events that are to be associated.

{{< note >}}
**Note:** To properly track and assess Events, the `arc_correlation_value` should be unique to each pair of Events.
{{< /note >}}

For example, "a Maintenance Request Event must be addressed by a Maintenance Performed Event".

{{< tabs name="compliance_current_outstanding" >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_CURRENT_OUTSTANDING policy
      print_response: true
    description: "There should be no outstanding Maintenance Requests"
    display_name: Outstanding Maintenance Requests
    compliance_type: COMPLIANCE_CURRENT_OUTSTANDING
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Request
    closing_event_display_type: Maintenance Performed
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_CURRENT_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests",
    "display_name": "Outstanding Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_home_location_identity=locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Request",
    "closing_event_display_type":  "Maintenance Performed"
}
```
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```
{{< /tab >}}}
{{< /tabs >}}

3. ***COMPLIANCE_PERIOD_OUTSTANDING:*** checks if the time between correlated Events does not exceed set threshold.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of Events that are to be associated.

{{< note >}}
**Note:** To properly track and assess Events, the `arc_correlation_value` should be unique to each pair of Events.
{{< /note >}}

For example, "a Maintenance Request Event must be addressed by a Maintenance Performed Event within 72 hours".

{{< tabs name="compliance_period_outstanding" >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_PERIOD_OUTSTANDING policy
      print_response: true
    description: There should not be outstanding Maintenance Requests for longer than 72hr
    display_name: Outstanding Maintenance Requests 72hr
    compliance_type: COMPLIANCE_PERIOD_OUTSTANDING
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Request
    closing_event_display_type: Maintenance Performed
    time_period_seconds: "259200"
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_PERIOD_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests longer than 72hr",
    "display_name": "Outstanding Maintenance Requests 72hr",
    "asset_filter": [
        { "or": ["attributes.arc_home_location_identity=locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Request",
    "closing_event_display_type":  "Maintenance Performed",
    "time_period_seconds": "259200"
}
```
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```
{{< /tab >}}}
{{< /tabs >}}

4. ***COMPLIANCE_DYNAMIC_TOLERANCE:*** checks that the time between correlated Events is not excessively different to the observed average normal duration for similar Events.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of Events that are to be associated.

{{< note >}}
**Note:** To properly track and assess Events, the `arc_correlation_value` should be unique to each pair of Events.
{{< /note >}}

For example, "the time between a Maintenance Request Event and Maintenance Performed Event in the last week does not exceed a variation of 0.5 standard deviations around the mean".

The `dynamic_window` is the time period to evaluate on, in this case, one week. The `dynamic_variability` is the number of standard deviations from the mean allowed, in this case, 0.5.

{{< tabs name="compliance_dynamic_tolerance" >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_DYNAMIC_TOLERANCE policy
      print_response: true
    description: Average time between Maintenance Requested/Performed
    display_name: Outlying Maintenance Requests
    compliance_type: COMPLIANCE_DYNAMIC_TOLERANCE
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Request
    closing_event_display_type: Maintenance Performed
    dynamic_window: "604800"
    dynamic_variability: "0.5"
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_DYNAMIC_TOLERANCE",
    "description": "Average time between Maintenance Requested/Performed",
    "display_name": "Outlying Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_home_location_identity=locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Request",
    "closing_event_display_type": "Maintenance Performed",
    "dynamic_window": 604800,
    "dynamic_variability": 0.5
}
```
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```
{{< /tab >}}}
{{< /tabs >}}

5. ***COMPLIANCE_RICHNESS:*** checks whether Attributes are within expected bounds or otherwise meet defined conditions.

This type of policy uses `richness_assertions`. An assertion is comprised of an attribute name, comparison value, and an operator to compare with.

The operator can be one of six relational operators: equal to (`=`), not equal to (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), less than or equal to (`<=`).

For example, "radiation level must be less than 7".

{{< tabs name="compliance_richness" >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Create COMPLIANCE_RICHNESS policy
      print_response: true
    description: "Radiation level must be less than 7"
    display_name: Rad Limit
    compliance_type: COMPLIANCE_RICHNESS
    asset_filter:
      - or: [ "attributes.arc_home_location_identity=locations/<location-id>" ]
    richness_assertions: 
      - or: [ "radiation_level<7" ]
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_RICHNESS",
    "description": "Rad level is less than 7",
    "display_name": "Rad Limit",
    "asset_filter": [
        { "or": ["attributes.arc_home_location_identity=locations/<location-id>"]}
    ],
    "richness_assertions": [
        { "or": ["radiation_level<7"]}
    ],
}
```
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v1/compliance_policies
```
{{< /tab >}}}
{{< /tabs >}}

## Checking Compliance Status

You may check the compliance status of a specific Asset within your tenancy.

{{< tabs name="compliance_status" >}}
{{< tab name="YAML" >}}
Create a yaml file, using the desired Asset ID as your `asset_label`. Setting `report: true` will print the compliance information for the Asset when the file is run. 

```yaml
---
steps:
  - step:
      action: COMPLIANCE_COMPLIANT_AT
      description: Check Compliance of desired Asset.
      asset_label: assets/<asset-id>
    report: true
```
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      <path-to-yaml-file>
```
{{< /tab >}}
{{< tab name="JSON" >}}
Run the following command using the desired Asset ID to check its compliance status. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v1/compliance/assets/<asset-id>
```

You may also determine compliance at a [historical date](/platform/overview/advanced-concepts/#perspectives) by adding the desired date to the query.

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    "https://app.rkvst.io/archivist/v1/compliance/assets/<asset-id>?compliant_at=2019-11-27T14:44:19Z"
```
{{< /tab >}}}
{{< /tabs >}}