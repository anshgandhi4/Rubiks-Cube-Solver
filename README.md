# Rubiks Cube Solver
This is the official repository for Rubiks Cube Solver.

Rubiks Cube Solver is program that scans a Rubik's Cube and gives a optimal solution to solve it.

## Notes:
**This repository is licensed under the GNU General Purpose License. A copy of the license is provided in this project under the name COPYING.txt. Please visit https://www.gnu.org/licenses/ for license details.**
**The solutions given by the program aren't the most efficient, but are still reasonably optimal.**

## How to Run This Code:
The solver can be run by using its original source code or by using a .exe file.

### Run Using Python
 1. Clone/fork this repository or download the .zip file (by clicking on the green "Code" button and clicking "Download ZIP").
 2. Make sure that you have a Python version of 3.6.x or later. You will also need the pip package installer.
 3. Use pip to install the following packages: opencv-python and kociemba. You can do this by running the following command: `pip install opencv-python kociemba`. You may need to download [Visual Studio C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) for the kociemba package if you get an error while installing it.
 4. The source code is now ready for you to modify and run. The main file to run is `main.py`. Enjoy!
 
### Run Using Executable
 1. Download the .zip file from the [releases section of this GitHub page](https://github.com/anshgandhi4/Rubiks-Cube-Solver/releases).
 2. Unzip the file and click on `main.exe` to run the solver. Enjoy!
 
## How to Use This Code:
 1. Once you have the script running, the first step is to scan the cube.
 2. Start by scanning the face with the white center towards the camera and the blue face facing upwards.
 3. Once the colors are detected correctly, move the slider to the next position.
 4. Rotate the cube so that the red face is facing the camera and the white face is facing upwards.
 5. Repeat Step 3.
 6. Rotate the cube so that the green face is facing the camera and the white face is facing upwards.
 7. Repeat Step 3.
 8. Rotate the cube so that the yellow face is facing the camera and the green face is facing upwards.
 9. Repeat Step 3.
 10. Rotate the cube so that the orange face is facing the camera and the white face is facing upwards.
 11. Repeat Step 3.
 12. Rotate the cube so that the blue face is facing the camera and the white face is facing upwards.
 13. Repeat Step 3.
 14. The camera screen and the slider should close. You will be left with a message on the command prompt window.
 15. The solve solution will be printed in [standard cubing notation](https://www.youtube.com/embed/24eHm4ri8WM?start=0&end=51).
 16. Follow the solution with white on the top and green in the front.
 17. If done correctly, your cube should be solved!
