---
title: "Creating an Asset"
description: "Creating your first Asset"
lead: "Creating your first Asset"
date: 2021-05-18T14:52:25+01:00
lastmod: 2021-05-18T14:52:25+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 21
toc: true
---

An Asset can be anything: a Connected Machine, a Shipping Container, or even a Data Set. It can be any physical or digital object with an associated Name, Description, and Attributes.

Each Asset will have a history of any actions performed upon it by any actor. 

The creation of an Asset is the first Event in its lifecycle. The following steps will guide you in creating your first Asset.

## Creating an Asset

1. Create your Asset. 

{{< tabs name="add_asset" >}}
{{{< tab name="UI" >}}
Using the Sidebar, select 'Add Asset'.
{{< img src="AssetAdd.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#To create your asset, use the action 'ASSETS_CREATE_IF_NOT_EXISTS'
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS

{{< /tab >}}}
{{< /tabs >}}

2. Add details to your new Asset.

{{< tabs name="add_asset_details" >}}
{{{< tab name="UI" >}}
You will see an Asset Creation form, where you provide details of your new Asset:
{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#Add details to your new Asset
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
      arc_description: Originally shipped from Shanghai
    location: 
      selector: 
        - display_name
      display_name: Parkside Junction
      description: Box intersection between Mill Road and East Road
      latitude: 53.4560
      longitude: 2.5895

{{< /tab >}}}
{{< /tabs >}}



3. At minimum, you will need to add an Asset Name and Asset Type to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My First Container'
* `Asset Type` - This is the class of the object; while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container, the type could be `Shipping Container` which will then be pre-populated for future Assets to use as their own types

{{< tabs name="add_asset_details_min" >}}
{{{< tab name="UI" >}}
{{< img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#arc_display_name and arc_display_type are recognized by RKVST as Asset Name and Asset Type
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
      arc_description: Originally shipped from Shanghai
    location: 
      selector: 
        - display_name
      display_name: Parkside Junction
      description: Box intersection between Mill Road and East Road
      latitude: 53.4560
      longitude: 2.5895

{{< /tab >}}}
{{< /tabs >}}



4. At this point, you may wish to add other details to your Asset, including attachments such as PDFs or Thumbnail Images. You may also wish to add Extended Attributes. 

Extended Attributes are user-defined and can be added to each unique Asset. 

Not all Assets of a specific type need to have the same Extended Attributes, but in most cases it is better to do so for consistency. 

To add a new Attribute to an Asset, enter your key-value pair.

For Example:

{{< tabs name="add_extended_attributes" >}}
{{{< tab name="UI" >}}
Select 'Add Attribute', and add your key-value pairs. 
{{< img src="AssetExtendedAttributes.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#See custom key-value pairs. 
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
      arc_description: Originally shipped from Shanghai
      Width: "2.43m"
      Length: "6.06m"
      Height: "2.59m"
    location: 
      selector: 
        - display_name
      display_name: Parkside Junction
      description: Box intersection between Mill Road and East Road
      latitude: 53.4560
      longitude: 2.5895

{{< /tab >}}}
{{< /tabs >}}



5. Complete your Asset creation.

{{< tabs name="finish_create_asset" >}}
{{{< tab name="UI" >}}
Click 'Create Asset'.
{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#Use 'confirm: true' to tell RKVST to finish commiting the asset before moving to the next step.  
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
      arc_description: Originally shipped from Shanghai
      Width: "2.43m"
      Length: "6.06m"
      Height: "2.59m"
    location: 
      selector: 
        - display_name
      display_name: Parkside Junction
      description: Box intersection between Mill Road and East Road
      latitude: 53.4560
      longitude: 2.5895
      confirm: true

{{< /tab >}}}
{{< /tabs >}}



6. View your Assets.


{{< tabs name="view_all_assets" >}}
{{{< tab name="UI" >}}
Navigate to 'Manage Assets' to see your Asset in the UI.
{{< img src="AssetManage.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#View your Assets using the 'ASSETS_LIST' action.  
---
steps:
  - step:
      action: ASSETS_LIST
      description: List all assets
      print_response: true

{{< /tab >}}}
{{< /tabs >}}


7. View details of the Asset you created.

{{< tabs name="view_specific_asset" >}}
{{{< tab name="UI" >}}
To view your Asset, click on the Asset row. You will see the detailed history of your Asset.
{{< img src="AssetView.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" codelang="yaml" >}}
#View your Asset using the 'ASSETS_LIST' action, with identifying attrs.  
---
steps:
  - step:
      action: ASSETS_LIST
      description: Display Asset named My First Container.
      print_response: true
    attrs:
      arc_display_name: My First Container

{{< /tab >}}}
{{< /tabs >}}



Here we see all details entered: The Extended Attributes and a history of Events recorded on the Asset.

The first Event will always be the Asset Creation. In the next section, we will cover how to create your own Events for your Asset.

