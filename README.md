# 🔍 Visualizing `.plt` Files with VisIt

You can directly visualize your solution files (`.plt`) using **[VisIt](https://visitusers.org/index.php?title=Downloading_and_Installing_VisIt)**, a powerful open-source visualization tool.

## ✅ Basic Steps to Plot

1. **Launch VisIt.**
2. Click **Open**, and **add** your `.plt` files.
3. Click **Add** → **Pseudocolor**, and select your desired **variable** (e.g., `u`).
4. Click **Draw** to visualize the plot.

## 🌄 3D Surface Visualization

To visualize in **3D** or create a **surface plot**:

1. Go to `Operators` → `Transforms` → `Elevate`.
2. After applying the elevate operator, go to `Operator Attributes` → `Transform` → `Elevate`.
3. Under **Scaling**:
   - Set **Auto-scaling** to `Never`.
   - Set **Elevate by variable** to your scalar field (e.g., `u`).

## 🧭 Customize Axis Labels and Annotations

To edit axis descriptions or plot annotations:

1. Navigate to `Controls` → `Annotation`.
2. Modify labels, fonts, ticks, or background as per your preference.

## Produce figures by running .py file
1. Run this as $visit -cli -nowin -s ./color.py sol sol.plt figure
2. This will create a file figure.ps, you can convert this to pdf by $ps2pdf figure.ps figure.pdf
3. For more details check the files .py

## 🛠️ Creating Your Own `.py` Plot Script from VisIt GUI

You can generate a custom plot style and export it as a Python script by following these steps:

1. **Open** the **VisIt GUI**.
2. **Load** your `.plt` file (e.g., `sol.plt`) and **draw the desired plot**.
3. **Go to** `Controls → Command`.
4. In the **Command** window:
   - Click **`Record`**.
   - Adjust the plot styling (e.g., color tables, view settings, annotations).
   - Click **`Stop`** once done.
5. The window will display the corresponding **Python commands**.
6. **Copy** the relevant portion and **save it** as a Python file, e.g., `color.py`.
7. **Run it** from the command line:

```bash
$ visit -cli -nowin -s ./color.py VariableName data.plt

