# 🔍 Visualizing `.plt` Files with VisIt

You can directly visualize your solution files (`.plt`) using **[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit)**, a powerful open-source visualization tool.

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
