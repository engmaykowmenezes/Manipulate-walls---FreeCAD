# Manipulate-walls-FreeCAD
Macros created with Python to automate the manipulation of architectural walls in FreeCAD

<h2>General description:</h2>
<p>These tools were created with the aim of facilitating the manipulation of wall elements within FreeCAD, and more specifically within the BIM Workbench. The tools manipulate the base geometry of the wall, so I strongly recommend that before moving the walls, activate the property to move the object base so that the tools work perfectly, the tools are in constant development and improvement, so there may be bugs, if you find any inconsistency please report it on my telegram @Eng_Maykow_Menezes or on my twitter <a href = "https://twitter.com/EngMaykow"  target=”_blank”>@EngMaykow</a>.</p>

<p>Note: Currently the tools only work for walls perpendicular to the Cartesian axes, which already covers most needs in architectural projects, in future versions this problem will be solved.</p>

<h2>Tools description:</h2>
<p>Distance between walls: This tool allows you to move a wall from another wall parallel to it. First select the wall that you want to move/distance, then select a wall parallel to the first to serve as a reference, activate the macro and then type the distance between the walls in mm in the box that will open, click “ok”, the wall will automatically be moved.<p>
  
<p>Trim wall: The trim wall tool allows you to separate a wall into two parts, the position of the cut occurs at the meeting of another wall perpendicular to the first one. Select the wall you want to split, then select a wall perpendicular to the first one to serve as the base of the cut (where the cut will be made), activate the macro, the wall will be split into two parts, you can delete or move each part individually .</p>

<p>Extend wall: This tool allows you to extend a wall to another wall, and also allows you to extend a wall a pre-defined distance. To extend a wall to another, proceed as follows, select the wall to be extended, select the wall that will serve as the base for the extension of the first one (this last selected wall must be perpendicular to the first), activate the macro, and the first wall will be extended to the second. To extend the wall a pre-defined distance, select the wall that you want to extend, in the dialog box that will open, type the distance you want to extend the wall and confirm by clicking ok (positive values extend the wall in the positive direction of the parallel axis the wall, negative values extend the wall in the negative direction of the axis parallel to the wall).</p>

<p>Indent wall: This tool works similarly to the previous one, however it only indents fixed values, it is not possible to indent a wall based on another. To retract a wall, select the wall to be retracted, activate the macro and in the dialog box that will open, enter the distance to retract the wall and confirm by clicking ok (positive values retract the side of the wall that is in the positive direction of the axis parallel to the wall, negative values indent the wall on the side of the wall that is in the negative direction of the axis parallel to the wall).</p>

<p>Separating walls: Have you noticed that when creating walls using the Wall tool from the BIM bench the walls are automatically grouped, this is very interesting to make the project more beautiful and more consistent, but to edit the walls the grouping of them becomes a nuisance, With that in mind, I developed a tool that automatically ungroups all the walls of the document in order to facilitate editing, after editing the walls you can join them again. To ungroup all the walls in the document, simply activate the macro, and automatically all the walls will be ungrouped. (This tool will change soon, as it is not interesting to ungroup all the walls of a model, I will implement a version that only ungroups the selected walls ).</p>

<h2>Installation with buttons and icons:</h2>
<p>To install the tools, download the files and copy them to your macros folder, (also copy the icons folder to the macros folder), go to Customize in the tools menu.</p>

<p>Na janela que se abrirá vá para a aba  “Macros”.</p>

<p>1 - Select a Macro and fill in the required fields.</p>

<p>2 - Click the button to select the icons.</p>

<p>3 - Click Icon Folder, and select the icon folder you copied to the macro folder (this procedure must be performed only once), confirm the folder selection.</p>

<p>4 - Select the icon corresponding to the tool you are installing.</p>

<p>5 - Click on add.</p>

<p>6 - Repeat steps 1, 2, 4 and 5 for each tool.</p>

<p>7 - Go to the “Toolbar” tab, on the right side Select the BIM Workbench and click on “New” and create a name for your toolbar.</p>

<p>8 - Then select the toolbar you just created and on the left side select the “Macros” option.</p>

<p>9 - Select the tools you want to install from the toolbar and click the right arrow.</p>

<p>10 - After installing all the tools in your Toolbar Click close and your tools will be installed, just start using.</p>

<h2>Installation without buttons and icons:</h2>
  
<p>To install your macros without buttons and icons, just copy all the files to your macros folder and access them through the Macros button.</p>

<h2>What may come in future updates.</h2>

<ul>
  <li>It is planned to implement in the tools support for walls not perpendicular to the axes (walls diagonally across the planes)</li>
  <li>Tool similar to Revit's Fillet tool, to create chamfers between walls or rounded corners.</li>
  <li>Tool to create stacked walls Similar to Revit.</li>
  <li>Tool to Link the top and bottom of walls to Levels.</li>
</ul>
