---
title: "Grouping Assets by Location"
description: "Adding a Location"
lead: "Adding a Location"
date: 2021-05-18T15:32:27+01:00
lastmod: 2021-05-18T15:32:27+01:00
draft: false
images: []
menu:
  docs:
    parent: "rkvst-basics"
weight: 34
toc: true
---

Locations associate an Asset with a 'home' that can help when governing sharing policies with OBAC and ABAC. Locations do not need pinpoint precision and can be named by site, building, or other logical grouping.

It may be useful to indicate an Asset's origin. For example, if tracking traveling consultant's Laptops, you may wish to associate them with a 'home' office.


## Creating a Location

1. Create your Location.


{{< tabs name="add_location_locations" >}}
{{{< tab name="UI" >}}
In the Dashboard, select `Add Location` in the Sidebar.
{{< img src="LocationAdd.png" alt="Rectangle" caption="<em>Adding a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The RKVST YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

In order to create a Location, we use the action `LOCATIONS_CREATE_IF_NOT_EXISTS`.
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
```
{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.
```json
{

}
```
{{< /tab >}}}
{{< /tabs >}}


2. Add information about the Location you are creating. 

{{< tabs name="add_location_info_locations" >}}
{{{< tab name="UI" >}}
The following screen will appear:
{{< img src="LocationDescribe.png" alt="Rectangle" caption="<em>The Location Webform</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
You may add a `description` and a `selector`. The `selector` is the identifying attribute used to check if your location exists before attempting to create it. In this case, we use `display_name` which represents the name of the Location.
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
```
{{< /tab >}}
{{< tab name="JSON" >}}
You may add a `display_name` and `description` to identify your Location.
 
```json
{
   "display_name": "UK Factory",
   "description": "Industrial Warehouse in Bristol Harbor"
}
```
{{< /tab >}}}
{{< /tabs >}}


3. Enter the required Location Name and Address, or in the case of YAML and JSON, coordinates.

{{< tabs name="add_location_name_locations" >}}
{{{< tab name="UI" >}}
{{< img src="LocationForm.png" alt="Rectangle" caption="<em>Adding the Location Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use `latitude` and `longitude` to describe the physical location. 
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
    display_name: UK Factory
    description: Industrial Warehouse in Bristol Harbor
    latitude: 51.4477
    longitude: -2.5980
```
{{< /tab >}}
{{< tab name="JSON" >}}
Use `latitude` and `longitude` to describe the physical location. 
 
```json
{
   "display_name": "UK Factory",
   "description": "Industrial Warehouse in Bristol Harbor",
   "lattitude": 51.4477,
   "longitude": -2.5980
}
```
{{< /tab >}}}
{{< /tabs >}}



4. There is an option to add Extended Attributes to a Location. This is useful to add metadata to a Location, i.e. a site contact's number and email address.

{{< tabs name="add_location_attributes_locations" >}}
{{{< tab name="UI" >}}
Use the `Extended Attributes` Tab.
{{< img src="LocationAttributes.png" alt="Rectangle" caption="<em>Adding Extended Attributes to a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Like Assets and Events, Locations may also have Extended Attributes added as key-value pairs. 
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
    display_name: UK Factory
    description: Factory in Bristol Harbor
    latitude: 51.4477
    longitude: -2.5980
    attributes:
      address: Princes Wharf, Wapping Rd, Bristol BS1 4RN, UK
      Primary_Contact: Jill Tiller
      Primary_Mobile_Number: +447700900077
```
{{< /tab >}}
{{< tab name="JSON" >}}
Like Assets and Events, Locations may also have Extended Attributes added as key-value pairs. 
 
```json
{
   "display_name": "UK Factory",
   "description": "Industrial Warehouse in Bristol Harbor",
   "lattitude": 51.4477,
   "longitude": -2.5980,
   "attributes": {
     "address": "Princes Wharf, Wapping Rd, Bristol BS1 4RN, UK",
     "Primary_Contact": "Jill Tiller",
     "Primary_Mobile_Number": "+447700900077"
   }
}
```
{{< /tab >}}}
{{< /tabs >}}




5. Complete your Location. 

{{< tabs name="complete_location_locations" >}}
{{{< tab name="UI" >}}
Click `Create Location`.
{{< img src="LocationSubmitted.png" alt="Rectangle" caption="<em>Submitting a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret <your-client-secret> \
      UK_factory_location.yaml
```
{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/locations
```
{{< /tab >}}}
{{< /tabs >}}


6. Navigate to `Manage Locations` in the Sidebar to see a list of existing Locations.
{{< img src="LocationView.png" alt="Rectangle" caption="<em>Managing a Location</em>" class="border-0" >}}

7. You can inspect details of a single Location. Click the desired Location row. 
{{< img src="LocationDetails.png" alt="Rectangle" caption="<em>Viewing a Location</em>" class="border-0" >}}


## Assigning a Location to an Asset

### Adding at Asset Creation

1. To assign a pre-existing Location to an Asset during Asset creation, you need only select it. 

{{< tabs name="add_at_asset_create" >}}
{{{< tab name="UI" >}}
Choose the desired Location from the Location drop-down.
{{< img src="LocationAssetCreation.png" alt="Rectangle" caption="<em>Creating an Asset with an Existing Location</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
A pre-exisiting Location can be added during Asset creation, using the Location ID as an identifier (e.g. `locations/<UUID>`). 
```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset with pre-existing Location. 
      asset_label: My First Container 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    attributes: 
      arc_display_name: My First Container
      arc_display_type: Shipping Container
      arc_home_location_identity: <your-location-id>
    confirm: true
```
The YAML Runner also allows you to create new locations at Asset Creation.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My First Container 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    attributes: 
      arc_display_name: My First Container
      arc_display_type: Shipping Container
    location: 
      selector: 
        - display_name
      display_name: UK Factory
      description: Container Origin
      latitude: 52.2025
      longitude: 0.1311
      attributes: 
        action: LOCATIONS_CREATE_IF_NOT_EXISTS
        location_label: UK Factory
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}
A pre-exisiting Location can be added during Asset creation, using the Location ID as an identifier (e.g. `locations/<UUID>`). 
```json
{
    "behaviours": ["RecordEvidence", "Attachments"],
    "attributes": {
        "arc_display_name": "My First Container",
        "arc_display_type": "Traffic light with violation camera",
        "arc_home_location_identity": "locations/<location-id>"
    }
}
```
{{< /tab >}}}
{{< /tabs >}}



### Adding to a pre-existing Asset

1. To assign a pre-existing asset with a new Location, you need to identify the Location Identity. To do this, view the Location details by clicking the Location row. 

{{< img src="LocationIdentity.png" alt="Rectangle" caption="<em>Location Identity</em>" class="border-0" >}}

2. Then create an Event for the Asset and specify the identity of the new Location as noted in step 1, against the `arc_home_location_identity` key. 

For more information on creating Events, please visit [Creating an Event Against an Asset](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/).

{{< tabs name="add_to_asset" >}}
{{{< tab name="UI" >}}

{{< img src="LocationAssetUpdate.png" alt="Rectangle" caption="<em>Updating an Existing Asset with a new Location</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note** - The `EVENTS_CREATE` action must contain at least one key-value pair for `event_attributes`.
{{< /note >}}

```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Add Location to existing Asset.
      asset_label: assets/<asset-id> 
    operation: Record
    behaviour: RecordEvidence
    event_attributes: 
      new_event: Record Asset Location
    asset_attributes:
      arc_home_location_identity: locations/<location-id>
    confirm: true
```

{{< /tab >}}
{{< tab name="JSON" >}}

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "asset_attributes": {
    "arc_home_location_identity": "locations/<location-id>"
  }
}
```
{{< note >}}
**Note** - The Event must be recorded against the appropriate `assets/<asset-id>` when the curl command is executed. [See Step 4 here for more details.](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/)
{{< /note >}}

{{< /tab >}}}
{{< /tabs >}}


{{< note >}}
**Note** - You need to include the full `locations/<UUID>` reference as using only the `UUID` will not be recognized.
{{< /note >}}

3. In the following screenshot, note the Location of our Asset has been updated.

{{< img src="LocationUpdateComplete.png" alt="Rectangle" caption="<em>Completed update of Asset Location</em>" class="border-0" >}}

