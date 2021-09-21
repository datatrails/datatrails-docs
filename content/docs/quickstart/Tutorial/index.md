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

1. Using the Sidebar, select `Add Asset`.

{{< img src="AssetAddNT.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}

2. You will see an Asset Creation form, where you provide details of your new Asset:

{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}

3. At minimum, you will need to add an Asset Name, Asset Type and Proof Mechanisim when using the UI to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My Bike'
* `Asset Type` - This is the type of Asset, while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a bike, the type could be `Bike` which will then be pre-populated for future Assets to use as their own types
* `Proof Mechanism` - This identifies storage to be used for an Asset. Khipu indicates the Asset will be stored via blockchain. Simple Hash indicates the Asset will be stored within RKVST tenancy.

{{< img src="AssetCreationDetailsQS.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}

4. You may wish to add other details to your Asset including attachments and Extended Attributes. 

Extended Attributes are user-defined and can be added to each unique Asset. 
To add a new Attribute to an Asset select `Add Attribute` then enter your key-value pair.

For Example:

{{< img src="AssetExtendedAttributesQS.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}

To add an attachment, select `Add Attchment` and then select the plus symbol.

{{< img src="AssetAttachmentQS.png" alt="Rectangle" caption="<em>Asset Attachment</em>" class="border-0" >}}

5. Once complete, click `Create Asset`

{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}

6. `Manage Assets` (default view) is where one can see their Asset within the UI.

{{< img src="AssetManageQS.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}

7. To view your Asset, click on the small eye symbol ( ![](EyeSymbol.png) ) to the right of the Asset in the Manage view. You will see the detailed history of your Asset.

{{< img src="AssetViewQS.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}

Here we see all details entered: The Extended Attributes and a history of Events recorded on the Asset.

The first Event will always be the Asset Creation, in the next section we will cover how to create your own Events for your Asset.

## Adding External Organizations to Allow Sharing

In order to share Assets and their details with another Organization or Tenant we must first import the ID of the External Organization.

### Finding Your Own ID

1. As a Root User, navigate to `Access Policies`

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and your Organization's ID will be contained within the `Self` box.

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing another Organization's ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and then `Import Subject`.

{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}

3. You will be presented with a form, the `Subject String` is the ID of the Organization with which you wish to share Asset evidence. The `Name` is a Friendly Name for you to label the imported organization.

{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}

## Creating an OBAC Sharing Policy

1. Navigate to the `Access Policies` section on the Sidebar of the RKVST User Interface.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Here you will see any existing policies, select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a policy the following form will appear:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying filters to your Policy for the right assets. In this case we're going to filter for Bike Assets in the `Jitsuin Paris` Location created earlier.

{{< img src="PolicyOBACFilterNT.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next we select the `Permissions` Tab to set which Organizations can read and write certain Asset attributes, as well as Event visibility.

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In our case we want the `Organization` actor which implies OBAC. Type the Friendly Name of the Organization we wish to share with into the box and we should see a prepopulated drop-down search.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that Organization. {{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. When the relevant controls are in place we then add the Permisson Group to the policy.

Note we have included RKVST-significant atributes: `arc_display_name` and `arc_display_type` which brings visibility to the Name and Type of Asset being shared. 

{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, submit the policy and check the Asset is shared appropriately; Mandy should only be able to see the Name and Type of Asset as well as the Asset's custom `Frame Color` attribute.

{{< img src="PolicyOBACMandyViewNT.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

By comparison our Root User, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillViewNT.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

9. If Mandy wishes to share what she can to Non-Root Users within her organization, it is her responsibility to create an ABAC Policy as she would any other Asset she has access to.

ABAC and OBAC Policy Creation has many fine-grained controls, to find out more, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/).

## Creating Events

1. When viewing your Asset click the `Record Event` button.

{{< img src="EventRecordNT.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}

2. You will see the following screen, where you can enter an Event type and description.

{{< img src="EventInformation.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}

3. Tabs enable you to enter both Event and Asset attributes.

* `Event Attributes` - Attributes specific to an Event e.g. signifying when the frame was ordered
* `Asset Attributes` - Attributes of the Asset that may change as a result of the Event e.g. color of the frame

Select the `Add Attribute` button on each field to add your Key-Value pairs.

For example:

{{< img src="EventAttributesNT.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributesNT.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}

Here we see someone noted the frame has been ordered in the Event, and has also recorded the color of the frame using a newly defined `Frame Color` attribute.

Every Event has an automatically generated `timestamp_accepted` and `principal_accepted` attribute that records _when_ who performed what, as submitted to RKVST.

PDFs or images can be recorded with an Event in the same way as an Asset. 

This is useful for storing associated material for posterity. For example, each `Frame Order` Event can store the PDF document of the frame ordered for inspection. This allows historical compliance checking of Events.

4. Once you have entered all data, click the `Record Event` Button, to add to your Asset.

You will see that the Asset Attribute we changed is also recorded in the Asset View.

{{< img src="EventRecordedNT.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. Use the eye symbol ( ![](EyeSymbol.png) ) to inspect the Event:

{{< img src="EventViewNT.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we see the details entered earlier and also a tab that will show both the Event Attributes and Asset Attributes:

{{< img src="EventAttributeViewNT.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}
