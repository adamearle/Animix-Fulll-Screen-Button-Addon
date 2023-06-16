bl_info = {
    "name": "AniMix Fullscreen Button",
    "author": "Adam Earle",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "Topbar > Main Window",
    "description": "Adds fullscreen button to the far right of the topbar",
    "category": "UI",
}

import bpy

# Define function to draw the fullscreen button
def draw_fullscreen_button(self, context):
    if context.region.alignment == 'RIGHT': # This ensures the button is aligned to the far right
        layout = self.layout
        row = layout.row(align=True)
    
        # Add fullscreen toggle button to the top bar (icon only)
        row.operator("wm.window_fullscreen_toggle", emboss=False, icon='FULLSCREEN_ENTER', text="")

# Register function
def register():
    # Append draw_fullscreen_button to top bar
    bpy.types.TOPBAR_HT_upper_bar.append(draw_fullscreen_button)
    
# Unregister function
def unregister():
    # Remove draw_fullscreen_button from top bar
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_fullscreen_button)

# Main execution
if __name__ == "__main__":
    register()
