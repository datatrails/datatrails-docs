---
 title: "Compliance Policies"
 description: "Creating and Managing Compliance Policies"
 lead: "Creating and Managing Compliance Policies"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   docs:
     parent: "beyond-the-basics"
 weight: 42
 toc: true
---

Compliance policies are user-defined rule sets that Assets can be test against. Compliance policies only need to be created once; all applicable Assets will be tested against that policy thereafter. 

For example, a policy might assert that “Maintenance Alarm Events must be answered with a Maintenance Report Event, recorded within 72 hours of the alarm”. This creates a Compliance Policy in the system which any Asset can be tested against as needed.

RKVST allows for several types of Compliance Policies: 

1. ***COMPLIANCE_SINCE:*** checks the time elapsed since a specific type of Event has met a certain threshold. 

For example, "time since last maintenance must be less than 72 hours".

{{< tabs name="compliance_since" >}}
{{{< tab name="UI" >}}
{{< img src="ComplianceSinceAsset.png" alt="Rectangle" caption="<em>Add Asset Information</em>" class="border-0" >}}
{{< img src="ComplianceSinceCompliance.png" alt="Rectangle" caption="<em>Add Compliance Information</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Maintenance should be performed every 72h
      print_response: true
    display_name: Regular Maintenance
    compliance_type: COMPLIANCE_SINCE
    asset_filter:
      - or: [ "attributes.arc_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Performed
    time_period_seconds: "259200"
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_SINCE",
    "description": "Maintenance should be performed every 72h",
    "display_name": "Regular Maintenance",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Performed",
    "time_period_seconds": "259200"
}
```
{{< /tab >}}}
{{< /tabs >}}

2. ***COMPLIANCE_CURRENT_OUTSTANDING:*** checks if there is an answering Event addressing an outstanding Event.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of events that are to be associated.

For example, "a Maintenance Request Event must be answered by a Maintenance Performed Event".

{{< tabs name="compliance_current_outstanding" >}}
{{{< tab name="UI" >}}
{{< img src="ComplianceOutstandingAsset.png" alt="Rectangle" caption="<em>Add Asset Information</em>" class="border-0" >}}
{{< img src="ComplianceOutstandingCompliance.png" alt="Rectangle" caption="<em>Add Compliance Information</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: 'There should be no outstanding Maintenance Requests'
      print_response: true
    display_name: Outstanding Maintenance Requests
    compliance_type: COMPLIANCE_CURRENT_OUTSTANDING
    asset_filter:
      - or: [ "attributes.arc_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Requests
    closing_event_display_type: Maintenance Performed
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_CURRENT_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests",
    "display_name": "Outstanding Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type":  "Maintenance Performed"
}
```
{{< /tab >}}}
{{< /tabs >}}

3. ***COMPLIANCE_PERIOD_OUTSTANDING:*** checks if the time between correlated events does not exceed set threshold.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of events that are to be associated.

For example, "a Maintenance Request Event must be answered by a Maintenance Performed Event within 72 hours".

{{< tabs name="compliance_period_outstanding" >}}
{{{< tab name="UI" >}}
{{< img src="CompliancePeriodAsset.png" alt="Rectangle" caption="<em>Add Asset Information</em>" class="border-0" >}}
{{< img src="CompliancePeriodCompliance.png" alt="Rectangle" caption="<em>Add Compliance Information</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: 'There should be no outstanding Maintenance Requests longer than 72hr'
      print_response: true
    display_name: Outstanding Maintenance Requests 72hr
    compliance_type: COMPLIANCE_PERIOD_OUTSTANDING
    asset_filter:
      - or: [ "attributes.arc_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Requests
    closing_event_display_type: Maintenance Performed
    time_period_seconds: "259200"
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_PERIOD_OUTSTANDING",
    "description": "There should be no outstanding Maintenance Requests longer than 72hr",
    "display_name": "Outstanding Maintenance Requests 72hr",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type":  "Maintenance Performed",
    "time_period_seconds": "259200"
}
```
{{< /tab >}}}
{{< /tabs >}}

4. ***COMPLIANCE_DYNAMIC_TOLERANCE:*** checks if time between correlated events does not exceed defined variability.

To correlate Events, define the attribute `arc_correlation_value` in the Event Attributes and set it to the same value on each pair of events that are to be associated.

For example, "the time between a Maintanence Request Event and Maintanence Performed Event in the last week does not exceed a variation of 0.5 standard deviations around the mean".

{{< tabs name="compliance_dynamic_tolerance" >}}
{{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Average time between Maintenance Requested/Performed
      print_response: true
    display_name: Outlying Maintenance Requests
    compliance_type: COMPLIANCE_DYNAMIC_TOLERANCE
    asset_filter:
      - or: [ "attributes.arc_location_identity=locations/<location-id>" ]
    event_display_type: Maintenance Requests
    closing_event_display_type: Maintenance Performed
    dynamic_window: "604800"
    dynamic_variability: "0.5"
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_DYNAMIC_TOLERANCE",
    "description": "Average time between Maintenance Requested/Performed",
    "display_name": "Outlying Maintenance Requests",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/<location-id>"]}
    ],
    "event_display_type": "Maintenance Requests",
    "closing_event_display_type": "Maintenance Performed",
    "dynamic_window": 604800,
    "dynamic_variability": 0.5
}
```
{{< /tab >}}}
{{< /tabs >}}

5. ***COMPLIANCE_RICHNESS:*** checks if the assertions conducted on an attribute value pass.

This type of policy uses `richness_assertions`. An assertion is comprised of an attribute name, comparison value, and an operator to compare with.

The operator can be one of six relational operators: equal to (`=`), not equal to (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), less than or equal to (`<=`).

For example, "radiation level must be less than 7".

{{< tabs name="compliance_richness" >}}
{{{< tab name="YAML" >}}
```yaml
---
steps:
  - step:
      action: COMPLIANCE_POLICIES_CREATE
      description: Rad level is less than 7
      print_response: true
    display_name: Rad Limit
    compliance_type: COMPLIANCE_RICHNESS
    asset_filter:
      - or: [ "attributes.arc_location_identity=locations/<location-id>" ]
    richness_assertions: 
      - or: [ "radiation_level<7" ]
```
{{< /tab >}}
{{< tab name="JSON" >}}
```json
{
    "compliance_type": "COMPLIANCE_RICHNESS",
    "description": "Rad level is less than 7",
    "display_name": "Rad Limit",
    "asset_filter": [
        { "or": ["attributes.arc_location_identity:locations/<location-id>"]}
    ],
    "richness_assertions": [
        { "or": ["radiation_level<7"]}
    ],
}
```
{{< /tab >}}}
{{< /tabs >}}