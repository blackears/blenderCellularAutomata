#  This file is part of the Kitfox Blender Cellular Automa distribution (https://github.com/blackears/blenderCellularAutoma).
#  Copyright (c) 2021 Mark McKay
#  
#  This program is free software: you can redistribute it and/or modify  
#  it under the terms of the GNU General Public License as published by  
#  the Free Software Foundation, version 3.
# 
#  This program is distributed in the hope that it will be useful, but 
#  WITHOUT ANY WARRANTY; without even the implied warranty of 
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#  General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License 
#  along with this program. If not, see <http://www.gnu.org/licenses/>.



bl_info = {
    "name": "Cellular Automata Texture Generators",
    "description": "Use cellular automata algorithm to generate semi=random naturalistic textures.",
    "author": "Mark McKay",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
#    "wiki_url": "https://github.com/blackears/blenderCellularAutomata",
    "tracker_url": "https://github.com/blackears/blenderCellularAutomata",
    "category": "View 3D"
}

import bpy
import importlib


if "bpy" in locals():
    if "genImageRule30" in locals():
        importlib.reload(genImageRule30)
    else:
        from .operators import genImageRule30
        
else:
    from .operators import genImageRule30

def register():
    genImageRule30.register()


def unregister():
    genImageRule30.unregister()

