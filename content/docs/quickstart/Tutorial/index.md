---
title: "Tutorial"
description: ""
lead: ""
date: 2021-05-18T15:33:31+01:00
lastmod: 2021-05-18T15:33:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 26
toc: true
---

## Creating an Asset

{{< note >}}
**Note:** To use the YAML Runner you will need to install the `jitsuin-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

1. Create your Asset. 

{{< tabs name="add_asset" >}}
{{{< tab name="UI" >}}
Using the Sidebar, select 'Add Asset'.
{{< img src="AssetAddNT.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The RKVST YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

In order to create an asset, we use the action `ASSETS_CREATE_IF_NOT_EXISTS`.
 
```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
```
{{< /tab >}}}
{{< /tabs >}}



2. Add details to your new Asset.

{{< tabs name="add_asset_details" >}}
{{{< tab name="UI" >}}
You will see an Asset Creation form, where you provide details of your new Asset:
{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Here you can fill out some more metadata about your asset:
* `selector` is the identifying attribute the yaml runner will use to check if your asset exists already before attempting to create it, in this case we use `arc_display_name` which represents the name of the Asset.
* `behaviours` detail what class of events in your assets lifecycle you might wish to record; `RecordEvidence` and `Attachments` are the standard and recommended behaviours for all assets.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: My Bike 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
```
{{< /tab >}}}
{{< /tabs >}}



3. At minimum, you will need to add an Asset Name and Asset Type to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My First Container'.
* `Asset Type` - This is the class of the object; while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container, the type could be `Shipping Container` which will then be pre-populated for future Assets to use as their own types.

{{< tabs name="add_asset_details_min" >}}
{{{< tab name="UI" >}}
`Proof Mechanism` identifies how frequently Asset history information is committed to the blockchain. `Khipu` - or 'Transactional Immutability' - indicates that every Event is committed through smart contracts and immediately committed to the chain. `Simple Hash` - or 'Batched Immutability' - indicates that Events are processed in the RKVST tenancy and then periodically collected together and committed to the chain as a batch.

{{< img src="AssetCreationDetailsQS.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The RKVST API uses the reserved attributes `arc_display_name` and `arc_display_type`  to represent `Asset Name` and `Asset Type`respectively.
```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset of a bike. 
      asset_label: My Bike 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    attributes: 
      arc_display_name: My Bike 
      arc_display_type: Bike
```
The YAML Runner defaults to `Simple Hash` as its proof mechanism.

{{< /tab >}}}
{{< /tabs >}}

4. You may wish to add other details to your Asset, including Attachments and Extended Attributes. 

Extended Attributes are user-defined and added per unique Asset.

To add a new Attribute to an Asset, enter your key-value pair. You may also add an attachment, such as an image of your Asset.

{{< tabs name="add_extended_attributes" >}}
{{{< tab name="UI" >}}
Select `Add Attribute`, and add your key-value pairs. 
{{< img src="AssetExtendedAttributesQS.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}
To add an attachment, such as an image of your asset, select `Add Attachment`, then select the plus symbol.
{{< img src="AssetAttachmentQS.png" alt="Rectangle" caption="<em>Asset Attachment</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Extended Attributes are custom key-value pairs, such as `Top_Tube`, `Seat_Tube`, and `Head_Tube` you see below.

This example also adds a location to our asset, to find out more about Locations, [click here](../grouping-assets-by-location/).

The `attachments` argument indicates a file, file type, and file display name that will be attached to your Asset.

It's also good practice to include `confirm: true` which tells RKVST to finish commiting the asset before moving to the next step. 
```yaml 
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset of a bike. 
      asset_label: My Bike 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    attributes: 
      arc_display_name: My Bike 
      arc_display_type: Bike
      arc_description: Replacement frame and upgraded tires
      Top_Tube: 570mm
      Seat_Tube: 420mm
      Head_Tube: 112mm
    location: 
      selector: 
        - display_name
      display_name: My Bike 
      latitude: 30.2672
      longitude: -97.7431
      attributes:
        address: Austin, Texas
    attachments: 
      - filename: my_bike.png
        content_type: image/png
        display_name: my_bike_image
    confirm: true
```
{{< /tab >}}}
{{< /tabs >}}


5. Complete your Asset creation.

{{< tabs name="finish_create_asset" >}}
{{{< tab name="UI" >}}
Click 'Create Asset'.
{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) command to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret client_secret.txt \
      my_bike.yaml
```
{{< /tab >}}}
{{< /tabs >}}



6. View your Assets.

{{< tabs name="view_all_assets" >}}
{{{< tab name="UI" >}}
`Manage Assets` (default view) is where you may view a list of your Assets within the UI.
{{< img src="AssetManageQS.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
You can view all Asset data using the `ASSETS_LIST` action; use the `print_response` keyword to get the full output.
```yaml  
---
steps:
  - step:
      action: ASSETS_LIST
      description: List all assets.
      print_response: true
```
{{< /tab >}}}
{{< /tabs >}}


7. View details of the Asset you created.

{{< tabs name="view_specific_asset" >}}
{{{< tab name="UI" >}}
To view your Asset, click on the Asset row. You will see the detailed history of your Asset.
{{< img src="AssetViewQS.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The `ASSETS_LIST` action can be filtered using identifying `attrs` to view the details of a specific Asset.
```yaml  
---
steps:
  - step:
      action: ASSETS_LIST
      description: Display Asset named My Bike.
      print_response: true
    attrs:
      arc_display_name: My Bike
```

{{< /tab >}}}
{{< /tabs >}}

Here you will see the details entered earlier: The Extended Attributes and the history of any Events recorded on the Asset.

The first Event in an Asset's Lifecycle will always be the 'Asset Creation' Event. In the next section, you will find out how to create your own events against an Asset.

## Creating Events

1. When viewing your Asset, click the `Record Event` button.

{{< img src="EventRecordQS.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}

2. You will see the following form, where you can enter an Event `Type` and `Description`.

{{< img src="EventInformationQS.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}

3. Using the Tabs enables you to then enter both Event and Asset attributes.

* `Event Attributes` - Attributes specific to an Event i.e. signifying _when_ a new frame was ordered
* `Asset Attributes` - Attributes of the Asset that may change as a result of the Event i.e. the color of the new frame

Select the `Add Attribute` button on each field to add your own custom Key-Value pairs.

For example:

{{< img src="EventAttributesQS.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributesQS.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}

Here you see that someone noted a new frame has been ordered in the Event, and has also recorded the color of the frame using a newly defined `Frame Color` Asset Attribute.

Note that every Event will always have a `timestamp_accepted` and `principal_accepted` Event Attributes once created, which records _when_ _who_ performed what, as submitted to RKVST; this is added automatically at Event Creation.

Similarly, PDFs or images can also be attached to an Event in the same way as an Asset. 

Attaching files is beneficial when storing contextual and associated material for posterity. For example, each `Frame Order` Event may have a copy of the invoice for the new frame and a datasheet attached ready for historical inspection and compliance checking.

4. Once you have entered your data, click the `Record Event` Button, to add the Event to your Asset.

You will see that the Asset Attribute that changed is recorded in the Asset View.

{{< img src="EventRecordedQS.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. You can click the Event row to inspect the Event:

{{< img src="EventViewQS.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here are the details entered earlier and also a tab that will show both the Event Attributes and Asset Attributes:

{{< img src="EventAttributeViewNT.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}

## Adding External Organizations to Allow Sharing

A key aspect of RKVST is the ability to share specific information with multiple external parties, in order to achieve this, you must first import the ID of the External Organization.

### Finding Your Own ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab, where your own Organization's ID will be located in the `Self` box.

{{< caution >}} **Caution:** Please do not use the subject info obtained from the copy menu on the login button. {{< /caution >}}

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing External Organization's ID

Once you have an Asset defined, it can be shared both within your department or even to another organization, enhancing the multi-party sharing experience.

{{< note >}}
**Note:** You must request that any external organization you wish to share with find their own Organization's ID using the steps above and share it with you before you can begin sharing Asset data with them.
{{< /note >}}

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and then `Import Subject`.

{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}

3. You will be presented with a new form: `Subject String` is the ID of the Organization that you wish to share Asset evidence with, `Name` is a Friendly Name for you to label the imported organization.

{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}

## Creating an OBAC Sharing Policy

1. Navigate to the `Access Policies` section in the Sidebar.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Here you can manage your existing policies, but for now select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a policy the following form will appear:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. You should begin applying filters to your Policy so it applies to the correct assets. Following the example let's filter for `Bike` type Assets in the `Jitsuin Paris` Location.

{{< note >}}
**Note:** The applied filters should be an exact match to what has been recorded.  Following the above example, there should be an Asset Type of `Bike` and location of `Jitsuin Paris` within RKVST.
{{< /note >}}


{{< img src="PolicyOBACFilterNT.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Select the `Permissions` Tab and define which Organizations can read and write which Attributes and Events.

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In the example let's use the `Organization` actor, implying OBAC (Organization Based Access Control). 

Enter the Friendly Name of the Organization you wish to share with and a pre-populated, drop-down search of the Organizations you have already imported should appear.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that Organization. {{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. Once the relevant details are complete, add the Permission Group to the policy by selecting `Add Permission Group`.

Note that the examples includes RKVST-significant attributes: `arc_display_name` and `arc_display_type` which allows visibility to the External Organization of the Name and Type of Asset being shared. 

{{< img src="PolicyPermissionsQS.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, select `Create Policy` and check the Asset is shared appropriately.

{{< img src="PolicyOBACPermissionsQS.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}

Mandy should be able to see only the `Name` and `Type` of Asset and the Asset's custom `Frame Color` attribute.

{{< img src="PolicyOBACMandyViewNT.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

By comparison our own Tenancy's Root User, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillViewNT.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

9. If Mandy wishes to then share what she can with Non-Root Users in her organization, it is her responsibility to create an ABAC Policy as she would any other Asset.

ABAC and OBAC Policy Creation has many fine-grained controls, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/) to find out more.