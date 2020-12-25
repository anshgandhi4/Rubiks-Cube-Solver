#  Copyright © 2020 Ansh Gandhi
#
#  This file is part of Rubiks Cube Solver.
#
#  Rubiks Cube Solver is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Rubiks Cube Solver is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with NorRubiks Cube SolverCalBot.  If not, see <https://www.gnu.org/licenses/>.
#
#  Original Author: Ansh Gandhi
#  Original Source Code: <https://github.com/anshgandhi4/Rubiks-Cube-Solver/>
#
#  EVERYTHING ABOVE THIS LINE MUST BE KEPT AS IS UNDER GNU GPL LICENSE RULES.

import cv2
import numpy as np
import kociemba

cam = cv2.VideoCapture(0)
counter = 0

blue = green = red = orange = white = yellow = 0
hsvColors = {'Blue': [blue, [0, 100, 100], [30, 255, 255]], 'Green': [green, [30, 100, 100], [75, 255, 255]],
    'Red': [red, [118, 120, 120], [140, 255, 255]], 'Orange': [orange, [100, 120, 120], [118, 255, 255]], 'White': [white, [0, 0, 75], [180, 45, 255]],
    'Yellow': [yellow, [75, 100, 100], [100, 255, 255]]}
rgbColors = {'Blue': (255, 0, 0), 'Green': (0, 255, 0), 'Red': (0, 0, 255), 'Orange': (0, 125, 255),
    'White': (255, 255, 255), 'Yellow': (0, 255, 255)}
faces = {'Blue': 'B', 'Green': 'F', 'Red': 'R', 'Orange': 'L',
    'White': 'U', 'Yellow': 'D'}
data = [['' for i in range(9)] for j in range(6)]

cv2.namedWindow('Selection')

def nothing(para):
    pass

cv2.createTrackbar('Selection', 'Selection', 0, 6, nothing)
output = ''
scan = True

while scan:
    img = cam.read()[1]

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    for i in range(0, 3):
        for j in range(0, 3):
            x = 240 + 120 * j
            y = 105 + 120 * i
            bestColor = 'White'
            bestValue = 0
            for key in ['Blue', 'Green', 'Red', 'Orange', 'White', 'Yellow']:
                color = hsvColors[key]
                color[0] = cv2.inRange(hsv[y - 60 : y + 60, x - 60 : x + 60], np.array(color[1]), np.array(color[2]))
                cv2.morphologyEx(color[0], cv2.MORPH_OPEN, (1, 1), color[0])
                cv2.morphologyEx(color[0], cv2.MORPH_CLOSE, (1, 1), color[0])
                avg = np.average(color[0])
                if avg > bestValue:
                    bestValue = avg
                    bestColor = key
                # cv2.imshow(key, color[0])
            selection = cv2.getTrackbarPos('Selection', 'Selection')
            if selection != 6:
                data[selection][3 * i + j] = faces[bestColor]
                cv2.rectangle(img, (x - 60, y - 60), (x + 60, y + 60), rgbColors[bestColor], 3)
            else:
                output = ''
                for face in range(6):
                    output += ''.join(data[face])
                scan = False

    cv2.imshow('Rubik\'s Cube Test', img)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()

print('Solution: ' + kociemba.solve(output))
input('Press Enter to close')