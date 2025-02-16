{
  "Electrodynamics_Formulas": [
    {
      "id": 1,
      "name": "Faraday's Law of Electromagnetic Induction",
      "math_expression": {
        "integral_form": "\\oint \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d\\Phi_B}{dt}",
        "differential_form": "\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}"
      },
      "variables": [
        {"symbol": "E", "meaning": "Electric field strength", "unit": "V/m"},
        {"symbol": "\\Phi_B", "meaning": "Magnetic flux", "unit": "Wb"}
      ],
      "keywords": ["Electromagnetic induction", "Time-varying magnetic field", "Vortex electric field"],
      "constraints": "Applicable to quasi-static fields, ignoring displacement current"
    },
    {
      "id": 2,
      "name": "Maxwell-Ampère's Law",
      "math_expression": {
        "integral_form": "\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 (I + \\varepsilon_0 \\frac{d\\Phi_E}{dt})",
        "differential_form": "\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J} + \\mu_0 \\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}"
      },
      "variables": [
        {"symbol": "B", "meaning": "Magnetic induction", "unit": "T"},
        {"symbol": "I", "meaning": "Conduction current", "unit": "A"},
        {"symbol": "\\Phi_E", "meaning": "Electric flux", "unit": "V⋅m"},
        {"symbol": "J", "meaning": "Current density", "unit": "A/m²"},
        {"symbol": "\\mu_0", "meaning": "Permeability of free space", "unit": "H/m"},
        {"symbol": "\\varepsilon_0", "meaning": "Permittivity of free space", "unit": "F/m"}
      ],
      "keywords": ["Displacement current", "Continuity of total current", "Time-varying electric field"],
      "constraints": "Assumes linear, isotropic, and homogeneous media"
    },
    {
      "id": 3,
      "name": "Gauss's Law for Electricity",
      "math_expression": {
        "integral_form": "\\oint \\mathbf{E} \\cdot d\\mathbf{A} = \\frac{Q}{\\varepsilon_0}",
        "differential_form": "\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}"
      },
      "variables": [
        {"symbol": "E", "meaning": "Electric field strength", "unit": "V/m"},
        {"symbol": "Q", "meaning": "Enclosed charge", "unit": "C"},
        {"symbol": "\\rho", "meaning": "Charge density", "unit": "C/m³"},
        {"symbol": "\\varepsilon_0", "meaning": "Permittivity of free space", "unit": "F/m"}
      ],
      "keywords": ["Electric flux", "Charge distribution", "Electrostatic field"],
      "constraints": "Applicable to any closed surface"
    },
    {
      "id": 4,
      "name": "Gauss's Law for Magnetism",
      "math_expression": {
        "integral_form": "\\oint \\mathbf{B} \\cdot d\\mathbf{A} = 0",
        "differential_form": "\\nabla \\cdot \\mathbf{B} = 0"
      },
      "variables": [
        {"symbol": "B", "meaning": "Magnetic induction", "unit": "T"}
      ],
      "keywords": ["Magnetic flux", "Absence of magnetic monopoles", "Magnetic field lines are closed"],
      "constraints": "Applicable to any closed surface"
    },
    {
      "id": 5,
      "name": "Lorentz Force Law",
      "math_expression": "\\mathbf{F} = q(\\mathbf{E} + \\mathbf{v} \\times \\mathbf{B})",
      "variables": [
        {"symbol": "F", "meaning": "Lorentz force", "unit": "N"},
        {"symbol": "q", "meaning": "Charge of the particle", "unit": "C"},
        {"symbol": "E", "meaning": "Electric field", "unit": "V/m"},
        {"symbol": "v", "meaning": "Velocity of the particle", "unit": "m/s"},
        {"symbol": "B", "meaning": "Magnetic field", "unit": "T"}
      ],
      "keywords": ["Force on moving charge", "Electromagnetic force"],
      "constraints": "Relativistic effects may be important at high speeds"
    },
    {
      "id": 6,
      "name": "Biot-Savart Law",
      "math_expression": "d\\mathbf{B} = \\frac{\\mu_0}{4\\pi} \\frac{Id\\mathbf{l} \\times \\mathbf{r}}{r^3}",
      "variables": [
        {"symbol": "dB", "meaning": "Magnetic field contribution", "unit": "T"},
        {"symbol": "I", "meaning": "Current", "unit": "A"},
        {"symbol": "dl", "meaning": "Infinitesimal current element", "unit": "m"},
        {"symbol": "r", "meaning": "Distance vector from current element to point where field is measured", "unit": "m"},
        {"symbol": "\\mu_0", "meaning": "Permeability of free space", "unit": "H/m"}
      ],
      "keywords": ["Magnetic field from current", "Current distribution"],
      "constraints": "Steady currents"
    },
    {
      "id": 7,
      "name": "Poynting Theorem",
      "math_expression": "-\\frac{\\partial}{\\partial t} \\int_V (\\frac{1}{2} \\varepsilon_0 E^2 + \\frac{1}{2\\mu_0} B^2) dV = \\oint_S \\mathbf{S} \\cdot d\\mathbf{A} + \\int_V \\mathbf{J} \\cdot \\mathbf{E} dV",
      "variables": [
        {"symbol": "S", "meaning": "Poynting vector", "unit": "W/m²"},
        {"symbol": "E", "meaning": "Electric field", "unit": "V/m"},
        {"symbol": "B", "meaning": "Magnetic field", "unit": "T"},
        {"symbol": "J", "meaning": "Current density", "unit": "A/m²"},
        {"symbol": "V", "meaning": "Volume"},
        {"symbol": "A", "meaning": "Surface area"}
      ],
      "keywords": ["Energy conservation", "Electromagnetic energy flow", "Poynting vector"],
      "constraints": "Relates the energy stored in electromagnetic fields to the work done by the fields and the energy flux through a surface"
    },
    {
        "id": 8,
        "name": "Electromagnetic Potentials",
        "math_expression": {
            "scalar_potential": "\\mathbf{E} = -\\nabla \\phi - \\frac{\\partial \\mathbf{A}}{\\partial t}",
            "vector_potential": "\\mathbf{B} = \\nabla \\times \\mathbf{A}"
        },
        "variables": [
            {"symbol": "\\phi", "meaning": "Scalar potential", "unit": "V"},
            {"symbol": "A", "meaning": "Vector potential", "unit": "T⋅m"}
        ],
        "keywords": ["Another representation of electric and magnetic fields", "Simplifying calculations"],
        "constraints": "The electromagnetic field can be described using scalar and vector potentials"
    },
    {
        "id": 9,
        "name": "Gauge Transformation",
        "math_expression": {
            "scalar_potential_transformation": "\\phi' = \\phi - \\frac{\\partial \\Lambda}{\\partial t}",
            "vector_potential_transformation": "\\mathbf{A}' = \\mathbf{A} + \\nabla \\Lambda"
        },
        "variables": [
            {"symbol": "\\Lambda", "meaning": "Arbitrary scalar function", "unit": "None"}
        ],
        "keywords": ["Degrees of freedom of electromagnetic potentials", "No effect on physical results"],
        "constraints": "Gauge transformations do not change physical observables"
    },
    {
        "id": 10,
        "name": "Retarded Potentials",
        "math_expression": {
            "retarded_scalar_potential": "\\phi(\\mathbf{r}, t) = \\frac{1}{4\\pi\\varepsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t_r)}{|\\mathbf{r} - \\mathbf{r}'|} d^3r'",
            "retarded_vector_potential": "\\mathbf{A}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi} \\int \\frac{\\mathbf{J}(\\mathbf{r}', t_r)}{|\\mathbf{r} - \\mathbf{r}'|} d^3r'"
        },
        "variables": [
            {"symbol": "t_r", "meaning": "Retarded time", "unit": "s"},
            {"symbol": "r", "meaning": "Observer position", "unit": "m"},
            {"symbol": "r'", "meaning": "Source position", "unit": "m"}
        ],
        "keywords": ["Considering the time delay effect of electromagnetic wave propagation", "Non-static fields"],
        "constraints": "Applicable to non-static fields, considering the finite speed of electromagnetic wave propagation"
    },
    {
      "id": 11,
      "name": "电磁波方程 (Electromagnetic Wave Equation)",
      "math_expression": {
        "equation_for_E": "\\nabla^2 \\mathbf{E} - \\mu_0\\varepsilon_0 \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} = 0",
        "equation_for_B": "\\nabla^2 \\mathbf{B} - \\mu_0\\varepsilon_0 \\frac{\\partial^2 \\mathbf{B}}{\\partial t^2} = 0"
      },
      "variables": [
        {"symbol": "c", "meaning": "光速, $c = \\frac{1}{\\sqrt{\\mu_0\\varepsilon_0}}$", "unit": "m/s"}
      ],
      "keywords": ["电磁波的传播", "光速"],
      "constraints": "在真空中或均匀介质中"
    },
    {
      "id": 12,
      "name": "电磁波的能量和动量 (Energy and Momentum of Electromagnetic Waves)",
      "math_expression": {
        "energy_density": "u = \\frac{1}{2} \\varepsilon_0 E^2 + \\frac{1}{2\\mu_0} B^2",
        "Poynting_vector": "\\mathbf{S} = \\frac{1}{\\mu_0} \\mathbf{E} \\times \\mathbf{B}",
        "momentum_density": "\\mathbf{g} = \\frac{1}{c^2} \\mathbf{S}"
      },
      "variables": [
        {"symbol": "u", "meaning": "能量密度", "unit": "J/m³"},
        {"symbol": "S", "meaning": "坡印亭向量", "unit": "W/m²"},
        {"symbol": "g", "meaning": "动量密度", "unit": "kg⋅m/s²"}
      ],
      "keywords": ["电磁波携带能量和动量", "辐射"],
      "constraints": "描述电磁波的能量和动量特性"
    },
    {
      "id": 13,
      "name": "电偶极子辐射 (Electric Dipole Radiation)",
      "math_expression": {
        "electric_field": "\\mathbf{E}(\\mathbf{r}, t) = \\frac{p_0}{4\\pi\\varepsilon_0 r^3} [3(\\mathbf{p} \\cdot \\hat{\\mathbf{r}})\\hat{\\mathbf{r}} - \\mathbf{p}] + \\frac{\\mu_0}{4\\pi r} \\ddot{\\mathbf{p}}_\\perp",
        "magnetic_field": "\\mathbf{B}(\\mathbf{r}, t) = -\\frac{\\mu_0}{4\\pi c r} \\hat{\\mathbf{r}} \\times \\ddot{\\mathbf{p}}"
      },
      "variables": [
        {"symbol": "p", "meaning": "电偶极矩", "unit": "C⋅m"},
        {"symbol": "\\ddot{p}", "meaning": "电偶极矩的二阶时间导数", "unit": "C⋅m/s²"},
        {"symbol": "r", "meaning": "观察点到偶极子的距离", "unit": "m"},
        {"symbol": "\\hat{r}", "meaning": "从偶极子指向观察点的单位矢量", "unit": "无"},
        {"symbol": "⊥", "meaning": "垂直于 \\hat{r} 的分量", "unit": "无"}
      ],
      "keywords": ["电偶极子产生的电磁辐射", "远场近似"],
      "constraints": "适用于电偶极子尺寸远小于波长的远场区域"
    },
    {
      "id": 14,
      "name": "磁偶极子辐射 (Magnetic Dipole Radiation)",
      "math_expression": {
        "magnetic_field": "\\mathbf{B}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi r^3} [3(\\mathbf{m} \\cdot \\hat{\\mathbf{r}})\\hat{\\mathbf{r}} - \\mathbf{m}] - \\frac{\\mu_0}{4\\pi c^2 r} \\hat{\\mathbf{r}} \\times \\ddot{\\mathbf{m}}_\\perp",
        "electric_field": "\\mathbf{E}(\\mathbf{r}, t) = \\frac{1}{c} \\mathbf{B} \\times \\hat{\\mathbf{r}}"
      },
      "variables": [
        {"symbol": "m", "meaning": "磁偶极矩", "unit": "A⋅m²"},
        {"symbol": "\\ddot{m}", "meaning": "磁偶极矩的二阶时间导数", "unit": "A⋅m²/s²"}
      ],
      "keywords": ["磁偶极子产生的电磁辐射", "远场近似"],
      "constraints": "适用于磁偶极子尺寸远小于波长的远场区域"
    },
    {
      "id": 15,
      "name": "电磁波在介质中的传播 (Electromagnetic Waves in Media)",
      "math_expression": {
        "wave_equation_in_medium": "\\nabla^2 \\mathbf{E} - \\mu\\varepsilon \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} = 0",
        "refractive_index": "n = \\sqrt{\\frac{\\varepsilon}{\\varepsilon_0}}",
        "wave_velocity_in_medium": "v = \\frac{1}{\\sqrt{\\mu\\varepsilon}} = \\frac{c}{n}"
      },
      "variables": [
        {"symbol": "\\mu", "meaning": "介质的磁导率", "unit": "H/m"},
        {"symbol": "\\varepsilon", "meaning": "介质的介电常数", "unit": "F/m"},
        {"symbol": "n", "meaning": "折射率", "unit": "无"}
      ],
      "keywords": ["电磁波在介质中的传播速度", "折射率"],
      "constraints": "假设介质是均匀、线性、各向同性的"
    },
    {
      "id": 16,
      "name": "惠更斯-菲涅尔原理 (Huygens-Fresnel Principle)",
      "math_expression": "U(P) = \\iint_S U(Q) \\frac{e^{ikr}}{r} \\cos\\theta dS",
      "variables": [
        {"symbol": "U(P)", "meaning": "P点处的波函数", "unit": "无"},
        {"symbol": "U(Q)", "meaning": "Q点处的波函数", "unit": "无"},
        {"symbol": "r", "meaning": "Q点到P点的距离", "unit": "m"},
        {"symbol": "\\theta", "meaning": "Q点到P点的连线与法线之间的夹角", "unit": "rad"},
        {"symbol": "k", "meaning": "波数", "unit": "m⁻¹"}
      ],
      "keywords": ["波的衍射", "波前传播"],
      "constraints": "描述了波在传播过程中的衍射现象"
    },
    {
      "id": 17,
      "name": "克拉默斯-克朗尼希关系 (Kramers-Kronig Relations)",
      "math_expression": {
        "relation_1": "Re[\\varepsilon(\\omega)] = 1 + \\frac{2}{\\pi} \\int_0^\\infty \\frac{Im[\\varepsilon(\\omega')]}{\\omega' - \\omega^2} d\\omega'",
        "relation_2": "Im[\\varepsilon(\\omega)] = -\\frac{2\\omega}{\\pi} \\int_0^\\infty \\frac{Re[\\varepsilon(\\omega')] - 1}{\\omega' - \\omega^2} d\\omega'"
      },
      "variables": [
        {"symbol": "\\varepsilon(\\omega)", "meaning": "介质的复介电常数", "unit": "无"},
        {"symbol": "\\omega", "meaning": "角频率", "unit": "rad/s"}
      ],
      "keywords": ["介质的色散", "因果关系"],
      "constraints": "描述了介质的实部和虚部介电常数之间的关系，源于因果律"
    },
    {
      "id": 18,
      "name": "德拜公式 (Debye Formula)",
      "math_expression": "n^2 - 1 = \\frac{Ne^2}{m\\varepsilon_0} \\sum_j \\frac{f_j}{\\omega_0^2 - \\omega^2 - i\\gamma_j\\omega}",
      "variables": [
        {"symbol": "n", "meaning": "折射率", "unit": "无"},
        {"symbol": "N", "meaning": "分子数密度", "unit": "m⁻³"},
        {"symbol": "e", "meaning": "电子电荷", "unit": "C"},
        {"symbol": "m", "meaning": "电子质量", "unit": "kg"},
        {"symbol": "f_j", "meaning": "振子强度", "unit": "无"},
        {"symbol": "\\omega_0", "meaning": "共振频率", "unit": "rad/s"},
        {"symbol": "\\gamma_j", "meaning": "阻尼系数", "unit": "rad/s"}
      ],
      "keywords": ["介质的色散", "经典模型"],
      "constraints": "描述了介质的折射率与频率的关系，基于经典振子模型"
    },
    {
      "id": 19,
      "name": "切伦科夫辐射 (Cherenkov Radiation)",
      "math_expression": "\\cos\\theta = \\frac{1}{n\\beta}",
      "variables": [
        {"symbol": "\\theta", "meaning": "切伦科夫辐射的角度", "unit": "rad"},
        {"symbol": "n", "meaning": "介质的折射率", "unit": "无"},
        {"symbol": "\\beta", "meaning": "带电粒子的速度与光速之比", "unit": "无"}
      ],
      "keywords": ["带电粒子在介质中超光速运动", "电磁辐射"],
      "constraints": "当带电粒子在介质中以超光速运动时，会产生切伦科夫辐射"
    },
    {
      "id": 20,
      "name": "兰道-利夫希茨公式 (Landau-Lifshitz Formula)",
      "math_expression": "\\frac{d^2W}{d\\Omega d\\omega} = \\frac{e^2}{4\\pi^2c^3} \\left| \\int_{-\\infty}^{\\infty} [\\mathbf{n} \\times [(\\mathbf{n} - \\mathbf{v}) \\times \\dot{\\mathbf{v}}]] e^{i\\omega t} dt \\right|^2",
      "variables": [
        {"symbol": "W", "meaning": "辐射能量", "unit": "J"},
        {"symbol": "\\Omega", "meaning": "立体角", "unit": "sr"},
        {"symbol": "\\omega", "meaning": "角频率", "unit": "rad/s"},
        {"symbol": "n", "meaning": "观察方向的单位矢量", "unit": "无"},
        {"symbol": "v", "meaning": "带电粒子的速度", "unit": "m/s"},
        {"symbol": "\\dot{v}", "meaning": "带电粒子的加速度", "unit": "m/s²"}
      ],
      "keywords": ["带电粒子加速时的电磁辐射", "任意运动"],
      "constraints": "描述了任意运动的带电粒子辐射的电磁波的频谱和角分布"
    },
    {
      "id": 21,
      "name": "电磁场的变换 (Transformation of Electromagnetic Fields)",
      "math_expression": {
        "E_parallel": "E'_\parallel = E_\parallel",
        "E_perp": "E'_\perp = \\gamma(E_\perp + v \\times B)",
        "B_parallel": "B'_\parallel = B_\parallel",
        "B_perp": "B'_\perp = \\gamma(B_\perp - \\frac{v}{c^2} \\times E)"
      },
      "variables": [
        {"symbol": "E", "meaning": "电场", "unit": "V/m"},
        {"symbol": "B", "meaning": "磁场", "unit": "T"},
        {"symbol": "v", "meaning": "参考系相对速度", "unit": "m/s"},
        {"symbol": "\\gamma", "meaning": "洛伦兹因子, $\\gamma = \\frac{1}{\\sqrt{1 - \\frac{v^2}{c^2}}}$", "unit": "无"},
        {"symbol": "∥", "meaning": "平行于 v 的分量", "unit": "无"},
        {"symbol": "⊥", "meaning": "垂直于 v 的分量", "unit": "无"},
        {"symbol": "'", "meaning": "新参考系中的场", "unit": "无"}
      ],
      "keywords": ["相对论电动力学", "电磁场在不同参考系中的变换"],
      "constraints": "描述了电磁场在不同惯性参考系之间的变换关系"
    },
    {
      "id": 22,
      "name": "电磁场的协变形式 (Covariant Formulation of Electromagnetic Fields)",
      "math_expression": {
        "field_tensor": "F^{\\mu\\nu} = \\begin{pmatrix} 0 & -E_x/c & -E_y/c & -E_z/c \\\\ E_x/c & 0 & -B_z & B_y \\\\ E_y/c & B_z & 0 & -B_x \\\\ E_z/c & -B_y & B_x & 0 \\end{pmatrix}",
        "Maxwell's_equations": "\\partial_\\mu F^{\\mu\\nu} = \\mu_0 J^\\nu"
      },
      "variables": [
        {"symbol": "F^{\\mu\\nu}", "meaning": "电磁场张量", "unit": "无"},
        {"symbol": "J^\\nu", "meaning": "四维电流密度", "unit": "无"},
        {"symbol": "\\partial_\\mu", "meaning": "四维偏导数", "unit": "无"}
      ],
      "keywords": ["相对论电动力学", "麦克斯韦方程组的协变形式"],
      "constraints": "用四维张量形式描述电磁场和麦克斯韦方程组，更简洁优雅"
    },
    {
      "id": 23,
      "name": "作用量原理 (Action Principle)",
      "math_expression": "S = \\int L d^4x = -\\frac{1}{4\\mu_0} \\int F_{\\mu\\nu}F^{\\mu\\nu} d^4x - \\int A_\\mu J^\\mu d^4x",
      "variables": [
        {"symbol": "S", "meaning": "作用量", "unit": "J⋅s"},
        {"symbol": "L", "meaning": "拉格朗日量", "unit": "J/m³"},
        {"symbol": "A_\\mu", "meaning": "四维电磁势", "unit": "无"}
      ],
      "keywords": ["经典场论", "变分法"],
      "constraints": "电磁场可以通过最小化作用量来得到，这是一种更高级的描述电磁场的方法"
    },
    {
      "id": 28,
      "name": "电磁场的格林函数 (Green's Function for Electromagnetic Fields)",
      "math_expression": {
        "Green's_function_for_scalar_potential": "G(\\mathbf{r}, t; \\mathbf{r}', t') = \\frac{\\delta(t - t' - |\\mathbf{r} - \\mathbf{r}'|/c)}{4\\pi\\varepsilon_0 |\\mathbf{r} - \\mathbf{r}'|}",
        "Green's_function_for_vector_potential": "\\mathbf{G}(\\mathbf{r}, t; \\mathbf{r}', t') = \\frac{\\delta(t - t' - |\\mathbf{r} - \\mathbf{r}'|/c)}{4\\pi} \\frac{\\mu_0}{|\\mathbf{r} - \\mathbf{r}'|} \\mathbf{I}"
      },
      "variables": [
        {"symbol": "G", "meaning": "格林函数", "unit": "无"},
        {"symbol": "\\delta", "meaning": "狄拉克δ函数", "unit": "1/s"},
        {"symbol": "I", "meaning": "单位矩阵", "unit": "无"}
      ],
      "keywords": ["求解非均匀介质中的电磁场", "点源"],
      "constraints": "格林函数描述了点源产生的电磁场，可以用于求解非均匀介质中的电磁场"
    },
    {
      "id": 29,
      "name": "电磁场的散射 (Scattering of Electromagnetic Waves)",
      "math_expression": {
        "scattering_cross_section": "\\frac{d\\sigma}{d\\Omega} = |f(\\theta)|^2",
        "scattering_amplitude": "f(\\theta) = -\\frac{1}{4\\pi} \\int e^{-i\\mathbf{k}' \\cdot \\mathbf{r}} U(\\mathbf{r}) e^{i\\mathbf{k} \\cdot \\mathbf{r}} d^3r"
      },
      "variables": [
        {"symbol": "\\sigma", "meaning": "散射截面", "unit": "m²"},
        {"symbol": "\\Omega", "meaning": "立体角", "unit": "sr"},
        {"symbol": "f(\\theta)", "meaning": "散射振幅", "unit": "m"},
        {"symbol": "k", "meaning": "入射波的波数矢量", "unit": "m⁻¹"},
        {"symbol": "k'", "meaning": "散射波的波数矢量", "unit": "m⁻¹"},
        {"symbol": "U(\\mathbf{r})", "meaning": "散射势", "unit": "无"}
      ],
      "keywords": ["电磁波与物质相互作用", "经典散射"],
      "constraints": "描述了电磁波与物质相互作用时的散射现象，散射截面表示散射强弱"
    },
    {
      "id": 30,
      "name": "电磁场的吸收 (Absorption of Electromagnetic Waves)",
      "math_expression": {
        "absorption_coefficient": "\\alpha = \\frac{4\\pi k}{\\lambda}",
        "Beer-Lambert_law": "I = I_0 e^{-\\alpha x}"
      },
      "variables": [
        {"symbol": "\\alpha", "meaning": "吸收系数", "unit": "m⁻¹"},
        {"symbol": "k", "meaning": "虚部折射率", "unit": "无"},
        {"symbol": "\\lambda", "meaning": "波长", "unit": "m"},
        {"symbol": "I", "meaning": "透射光强度", "unit": "W/m²"},
        {"symbol": "I_0", "meaning": "入射光强度", "unit": "W/m²"},
        {"symbol": "x", "meaning": "介质厚度", "unit": "m"}
      ],
      "keywords": ["电磁波与物质相互作用", "能量吸收"],
      "constraints": "描述了电磁波在介质中传播时的能量吸收现象，吸收系数表示吸收强弱"
    },
    {
      "id": 31,
      "name": "电磁场的色散 (Dispersion of Electromagnetic Waves)",
      "math_expression": {
        "dispersion_relation": "n(\\omega) = \\sqrt{\\varepsilon(\\omega)}",
        "group_velocity": "v_g = \\frac{d\\omega}{dk} = \\frac{c}{n(\\omega) + \\omega \\frac{dn}{d\\omega}}"
      },
      "variables": [
        {"symbol": "n(\\omega)", "meaning": "与频率相关的折射率", "unit": "无"},
        {"symbol": "\\omega", "meaning": "角频率", "unit": "rad/s"},
        {"symbol": "v_g", "meaning": "群速度", "unit": "m/s"}
      ],
      "keywords": ["电磁波与物质相互作用", "频率依赖性"],
      "constraints": "描述了电磁波在介质中传播时的色散现象，群速度表示波包的传播速度"
    },
    {
      "id": 32,
      "name": "电磁场的边界条件 (Boundary Conditions for Electromagnetic Fields)",
      "math_expression": {
        "E_tangential": "E_{1t} - E_{2t} = 0",
        "E_normal": "E_{1n} - E_{2n} = \\frac{\\sigma}{\\varepsilon_0}",
        "B_tangential": "B_{1t} - B_{2t} = \\mu_0 K",
        "B_normal": "B_{1n} - B_{2n} = 0"
      },
      "variables": [
        {"symbol": "E", "meaning": "电场", "unit": "V/m"},
        {"symbol": "B", "meaning": "磁场", "unit": "T"},
        {"symbol": "\\sigma", "meaning": "面电荷密度", "unit": "C/m²"},
        {"symbol": "K", "meaning": "面电流密度", "unit": "A/m"},
        {"symbol": "1", "meaning": "介质1", "unit": "无"},
        {"symbol": "2", "meaning": "介质2", "unit": "无"},
        {"symbol": "t", "meaning": "切向分量", "unit": "无"},
        {"symbol": "n", "meaning": "法向分量", "unit": "无"}
      ],
      "keywords": ["电磁场在界面上的连续性", "界面条件"],
      "constraints": "描述了电磁场在不同介质分界面上的连续性条件"
    },
    {
      "id": 33,
      "name": "电磁场的唯一性定理 (Uniqueness Theorem for Electromagnetic Fields)",
      "math_expression": "在给定边界条件下，电磁场是唯一的",
      "variables": [],
      "keywords": ["电磁场的解的唯一性", "边界值问题"],
      "constraints": "在给定边界条件下，麦克斯韦方程组的解是唯一的"
    },
    {
      "id": 34,
      "name": "电磁场的互易定理 (Reciprocity Theorem for Electromagnetic Fields)",
      "math_expression": "\\int_V (\\mathbf{E}_1 \\cdot \\mathbf{J}_2 - \\mathbf{E}_2 \\cdot \\mathbf{J}_1) dV = 0",
      "variables": [
        {"symbol": "E_1", "meaning": "电场1", "unit": "V/m"},
        {"symbol": "J_1", "meaning": "电流密度1", "unit": "A/m²"},
        {"symbol": "E_2", "meaning": "电场2", "unit": "V/m"},
        {"symbol": "J_2", "meaning": "电流密度2", "unit": "A/m²"},
        {"symbol": "V", "meaning": "体积", "unit": "m³"}
      ],
      "keywords": ["电磁场的互易关系", "电磁场分析"],
      "constraints": "描述了电磁场在不同源分布下的互易关系"
    },
    {
      "id": 35,
      "name": "电磁场的等效原理 (Equivalence Principle for Electromagnetic Fields)",
      "math_expression": "电磁场可以等效为电荷分布和磁化分布产生的场",
      "variables": [],
      "keywords": ["电磁场的等效源", "电磁场计算"],
      "constraints": "描述了电磁场可以等效为电荷分布和磁化分布产生的场，这在电磁场计算中很有用"
    },
    {
      "id": 36,
      "name": "电磁场的共振 (Resonance of Electromagnetic Fields)",
      "math_expression": {
        "resonance_frequency": "\\omega_0 = \\frac{1}{\\sqrt{LC}}",
        "quality_factor": "Q = \\frac{\\omega_0}{2\\gamma}"
      },
      "variables": [
        {"symbol": "\\omega_0", "meaning": "共振频率", "unit": "rad/s"},
        {"symbol": "L", "meaning": "电感", "unit": "H"},
        {"symbol": "C", "meaning": "电容", "unit": "F"},
        {"symbol": "\\gamma", "meaning": "阻尼系数", "unit": "rad/s"}
      ],
      "keywords": ["电磁振荡", "能量损耗"],
      "constraints": "描述了电磁振荡电路的共振现象，共振频率表示能量交换最有效的频率"
    },
    {
      "id": 37,
      "name": "电磁场的阻尼 (Damping of Electromagnetic Fields)",
      "math_expression": {
        "damped_oscillation": "I(t) = I_0 e^{-\\gamma t} \\cos(\\omega t + \\phi)",
        "damping_coefficient": "\\gamma = \\frac{R}{2L}"
      },
      "variables": [
        {"symbol": "I(t)", "meaning": "电流随时间的变化", "unit": "A"},
        {"symbol": "I_0", "meaning": "初始电流", "unit": "A"},
        {"symbol": "R", "meaning": "电阻", "unit": "Ω"},
        {"symbol": "\\omega", "meaning": "振荡频率", "unit": "rad/s"},
        {"symbol": "\\phi", "meaning": "相位", "unit": "rad"}
      ],
      "keywords": ["电磁振荡", "能量损耗"],
      "constraints": "描述了电磁振荡电路的阻尼现象，阻尼系数表示能量损耗的快慢"
    },
    {
      "id": 38,
      "name": "电磁场的量子化 (Quantization of Electromagnetic Fields)",
      "math_expression": {
        "photon_energy": "E = \\hbar\\omega",
        "photon_momentum": "p = \\hbar k"
      },
      "variables": [
        {"symbol": "\\hbar", "meaning": "约化普朗克常数", "unit": "J⋅s"},
        {"symbol": "\\omega", "meaning": "角频率", "unit": "rad/s"},
        {"symbol": "k", "meaning": "波数", "unit": "m⁻¹"}
      ],
      "keywords": ["量子电动力学", "光子"],
      "constraints": "描述了电磁场的量子化特性，光子是电磁场的基本单元"
    },
    {
      "id": 39,
      "name": "电磁场的相互作用 (Interaction of Electromagnetic Fields with Matter)",
      "math_expression": {
        "force_on_a_charged_particle": "\\mathbf{F} = q(\\mathbf{E} + \\mathbf{v} \\times \\mathbf{B})",
        "energy_transfer": "\\Delta E = -q \\int \\mathbf{E} \\cdot d\\mathbf{l}"
      },
      "variables": [
        {"symbol": "q", "meaning": "电荷", "unit": "C"},
        {"symbol": "v", "meaning": "带电粒子的速度", "unit": "m/s"},
        {"symbol": "\\Delta E", "meaning": "能量变化", "unit": "J"}
      ],
      "keywords": ["带电粒子在电磁场中运动", "电磁力"],
      "constraints": "描述了带电粒子在电磁场中受到的力和能量变化"
    },
    {
      "id": 40,
      "name": "电磁场的辐射 (Radiation of Electromagnetic Fields)",
      "math_expression": {
        "Larmor_formula": "P = \\frac{\\mu_0 q^2 a^2}{6\\pi c}",
        "dipole_radiation": "P = \\frac{\\mu_0 \\ddot{p}^2}{12\\pi c^3}"
      },
      "variables": [
        {"symbol": "P", "meaning": "辐射功率", "unit": "W"},
        {"symbol": "q", "meaning": "电荷", "unit": "C"},
        {"symbol": "a", "meaning": "加速度", "unit": "m/s²"},
        {"symbol": "\\ddot{p}", "meaning": "电偶极矩的二阶时间导数", "unit": "C⋅m/s²"}
      ],
      "keywords": ["带电粒子加速时的电磁辐射", "偶极子辐射"],
      "constraints": "描述了带电粒子加速时产生的电磁辐射功率，Larmor 公式适用于任意带电粒子，偶极子辐射公式适用于电偶极子"
    },
    {
      "id": 41,
      "name": "电磁场的电磁力 (Electromagnetic Force)",
      "math_expression": {
        "Lorentz_force": "\\mathbf{F} = q(\\mathbf{E} + \\mathbf{v} \\times \\mathbf{B})",
        "force_on_a_current_carrying_wire": "\\mathbf{F} = I \\mathbf{l} \\times \\mathbf{B}"
      },
      "variables": [
        {"symbol": "F", "meaning": "电磁力", "unit": "N"},
        {"symbol": "q", "meaning": "电荷", "unit": "C"},
        {"symbol": "E", "meaning": "电场", "unit": "V/m"},
        {"symbol": "v", "meaning": "带电粒子的速度", "unit": "m/s"},
        {"symbol": "B", "meaning": "磁场", "unit": "T"},
        {"symbol": "I", "meaning": "电流", "unit": "A"},
        {"symbol": "l", "meaning": "导线长度", "unit": "m"}
      ],
      "keywords": ["带电粒子在电磁场中受力", "安培力"],
      "constraints": "描述了带电粒子在电磁场中受到的洛伦兹力，以及电流在磁场中受到的安培力"
    }, 
    {
      "id": 42,
      "name": "电磁场的角动量 (Angular Momentum of Electromagnetic Fields)",
      "math_expression": {
        "angular_momentum_density": "\\mathbf{l} = \\mathbf{r} \\times \\mathbf{g}",
        "total_angular_momentum": "\\mathbf{L} = \\int \\mathbf{l} d^3r"
      },
      "variables": [
        {"symbol": "l", "meaning": "角动量密度", "unit": "kg⋅m²/s"},
        {"symbol": "L", "meaning": "总角动量", "unit": "kg⋅m²/s"},
        {"symbol": "r", "meaning": "位置矢量", "unit": "m"},
        {"symbol": "g", "meaning": "动量密度", "unit": "kg⋅m/s²"}
      ],
      "keywords": ["电磁场角动量", "电磁波的角动量"],
      "constraints": "描述了电磁场的角动量密度和总角动量，电磁波也可以携带角动量"
    },
    {
      "id": 43,
      "name": "电磁场的极化 (Polarization of Electromagnetic Fields)",
      "math_expression": {
        "linear_polarization": "\\mathbf{E} = E_0 (\\hat{\\mathbf{x}} \\cos(\\omega t - kz) + \\hat{\\mathbf{y}} \\cos(\\omega t - kz))",
        "circular_polarization": "\\mathbf{E} = E_0 (\\hat{\\mathbf{x}} \\cos(\\omega t - kz) \\pm \\hat{\\mathbf{y}} \\sin(\\omega t - kz))",
        "elliptical_polarization": "\\mathbf{E} = E_0 (\\hat{\\mathbf{x}} \\cos(\\omega t - kz) + \\hat{\\mathbf{y}} \\sin(\\omega t - kz))"
      },
      "variables": [
        {"symbol": "E", "meaning": "电场", "unit": "V/m"},
        {"symbol": "E_0", "meaning": "电场振幅", "unit": "V/m"},
        {"symbol": "\\omega", "meaning": "角频率", "unit": "rad/s"},
        {"symbol": "k", "meaning": "波数", "unit": "m⁻¹"},
        {"symbol": "x", "meaning": "x方向单位矢量", "unit": "无"},
        {"symbol": "y", "meaning": "y方向单位矢量", "unit": "无"}
      ],
      "keywords": ["电磁波的偏振状态", "线偏振", "圆偏振", "椭圆偏振"],
      "constraints": "描述了电磁波的偏振状态，包括线偏振、圆偏振和椭圆偏振"
    },
    {
      "id": 44,
      "name": "电磁场的干涉 (Interference of Electromagnetic Fields)",
      "math_expression": {
        "constructive_interference": "\\Delta \\phi = 2n\\pi",
        "destructive_interference": "\\Delta \\phi = (2n+1)\\pi"
      },
      "variables": [
        {"symbol": "\\Delta \\phi", "meaning": "相位差", "unit": "rad"},
        {"symbol": "n", "meaning": "整数", "unit": "无"}
      ],
      "keywords": ["电磁波的干涉现象", "相干叠加"],
      "constraints": "描述了电磁波的干涉现象，包括相长干涉和相消干涉"
    },
    {
      "id": 45,
      "name": "电磁场的衍射 (Diffraction of Electromagnetic Fields)",
      "math_expression": {
        "single_slit_diffraction": "I(\\theta) = I_0 \\left( \\frac{\\sin(\\beta/2)}{\\beta/2} \\right)^2",
        "double_slit_diffraction": "I(\\theta) = I_0 \\cos^2(\\delta/2) \\left( \\frac{\\sin(\\beta/2)}{\\beta/2} \\right)^2"
      },
      "variables": [
        {"symbol": "I(\\theta)", "meaning": "衍射强度", "unit": "W/m²"},
        {"symbol": "I_0", "meaning": "最大强度", "unit": "W/m²"},
        {"symbol": "\\beta", "meaning": "相位差", "unit": "rad"},
        {"symbol": "\\delta", "meaning": "相位差", "unit": "rad"}
      ],
      "keywords": ["电磁波的衍射现象", "惠更斯-菲涅尔原理"],
      "constraints": "描述了电磁波的衍射现象，包括单缝衍射和双缝衍射"
    },
 {
      "id": 46,
      "name": "菲涅尔方程",
      "math_expression": {
        "s-polarization": {
          "reflection_coefficient": "r_s = \\frac{n_1 \\cos\\theta_1 - n_2 \\cos\\theta_2}{n_1 \\cos\\theta_1 + n_2 \\cos\\theta_2}",
          "transmission_coefficient": "t_s = \\frac{2n_1 \\cos\\theta_1}{n_1 \\cos\\theta_1 + n_2 \\cos\\theta_2}"
        },
        "p-polarization": {
          "reflection_coefficient": "r_p = \\frac{n_2 \\cos\\theta_1 - n_1 \\cos\\theta_2}{n_2 \\cos\\theta_1 + n_1 \\cos\\theta_2}",
          "transmission_coefficient": "t_p = \\frac{2n_1 \\cos\\theta_1}{n_2 \\cos\\theta_1 + n_1 \\cos\\theta_2}"
        }
      },
      "variables": [
        {"symbol": "r_s", "meaning": "s偏振光的反射系数", "unit": "无"},
        {"symbol": "t_s", "meaning": "s偏振光的透射系数", "unit": "无"},
        {"symbol": "r_p", "meaning": "p偏振光的反射系数", "unit": "无"},
        {"symbol": "t_p", "meaning": "p偏振光的透射系数", "unit": "无"},
        {"symbol": "n_1", "meaning": "介质1的折射率", "unit": "无"},
        {"symbol": "n_2", "meaning": "介质2的折射率", "unit": "无"},
        {"symbol": "\\theta_1", "meaning": "入射角", "unit": "rad"},
        {"symbol": "\\theta_2", "meaning": "折射角", "unit": "rad"}
      ],
      "keywords": ["电磁波的折射和反射", "s偏振", "p偏振"],
      "constraints": "描述了光在两种介质界面上的反射和透射行为，考虑了光的偏振状态"
    },
    {
        "id": 47,
        "name": "散度 of 旋度",
        "math_expression": {
        "differential_form": "\nabla \cdot (\nabla \times \mathbf{A}) = 0"
        },
        "variables": [
        {"symbol": "\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"}
        ],
        "keywords": ["散度", "旋度", "矢量微积分"],
        "constraints": "矢量场 \(\mathbf{A}\) 在定义域内可微"
    },
    {
        "id": 48,
        "name": "散度的定义",
        "math_expression": {
        "integral_form": "\lim_{V \to 0} \frac{1}{V} \oint_S \mathbf{A} \cdot d\mathbf{S} = \nabla \cdot \mathbf{A}"
        },
        "variables": [
        {"symbol": "\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "V", "meaning": "体积", "unit": "m³"},
        {"symbol": "S", "meaning": "表面", "unit": "m²"}
        ],
        "keywords": ["散度", "矢量微积分", "Gauss 定理"],
        "constraints": "矢量场 \(\mathbf{A}\) 在封闭曲面内连续且可微"
    },
    {
        "id": 49,
        "name": "旋度的 Cartesian 坐标表达式",
        "math_expression": {
        "differential_form": "\nabla \times \mathbf{A} = \left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right) \mathbf{\hat{i}} + \left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right) \mathbf{\hat{j}} + \left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) \mathbf{\hat{k}}"
        },
        "variables": [
        {"symbol": "\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "A_x", "meaning": "矢量场在 x 方向的分量", "unit": "根据具体情况"},
        {"symbol": "A_y", "meaning": "矢量场在 y 方向的分量", "unit": "根据具体情况"},
        {"symbol": "A_z", "meaning": "矢量场在 z 方向的分量", "unit": "根据具体情况"},
        {"symbol": "\mathbf{\hat{i}}", "meaning": "x 方向的单位矢量", "unit": "无单位"},
        {"symbol": "\mathbf{\hat{j}}", "meaning": "y 方向的单位矢量", "unit": "无单位"},
        {"symbol": "\mathbf{\hat{k}}", "meaning": "z 方向的单位矢量", "unit": "无单位"}
        ],
        "keywords": ["旋度", "矢量微积分", "Cartesian 坐标"],
        "constraints": "矢量场 \(\mathbf{A}\) 在 Cartesian 坐标系下可微"
    },
    {
        "id": 50,
        "name": "Gradient 的 Cartesian 坐标表达式",
        "math_expression": {
        "differential_form": "\nabla \phi = \frac{\partial \phi}{\partial x} \mathbf{\hat{i}} + \frac{\partial \phi}{\partial y} \mathbf{\hat{j}} + \frac{\partial \phi}{\partial z} \mathbf{\hat{k}}"
        },
        "variables": [
        {"symbol": "\phi", "meaning": "标量场", "unit": "根据具体情况"},
        {"symbol": "\nabla \phi", "meaning": "标量场的 Gradient", "unit": "根据具体情况"},
        {"symbol": "\mathbf{\hat{i}}", "meaning": "x 方向的单位矢量", "unit": "无单位"},
        {"symbol": "\mathbf{\hat{j}}", "meaning": "y 方向的单位矢量", "unit": "无单位"},
        {"symbol": "\mathbf{\hat{k}}", "meaning": "z 方向的单位矢量", "unit": "无单位"}
        ],
        "keywords": ["Gradient", "矢量微积分", "Cartesian 坐标"],
        "constraints": "标量场 \(\phi\) 在 Cartesian 坐标系下可微"
    },
    {
        "id": 51,
        "name": "Laplacian 的 Cartesian 坐标表达式",
        "math_expression": {
        "differential_form": "\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2}"
        },
        "variables": [
        {"symbol": "\phi", "meaning": "标量场", "unit": "根据具体情况"},
        {"symbol": "\nabla^2 \phi", "meaning": "标量场的 Laplacian", "unit": "根据具体情况"}
        ],
        "keywords": ["Laplacian", "矢量微积分", "Cartesian 坐标"],
        "constraints": "标量场 \(\phi\) 在 Cartesian 坐标系下二次可微"
    },
    {
        "id": 52,
        "name": "矢量场的 Laplacian 表达式",
        "math_expression": {
        "differential_form": "\nabla^2 \mathbf{A} = \nabla (\nabla \cdot \mathbf{A}) - \nabla \times (\nabla \times \mathbf{A})"
        },
        "variables": [
        {"symbol": "\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "\nabla^2 \mathbf{A}", "meaning": "矢量场的 Laplacian", "unit": "根据具体情况"}
        ],
        "keywords": ["矢量 Laplacian", "矢量微积分", "Cartesian 坐标"],
        "constraints": "矢量场 \(\mathbf{A}\) 在 Cartesian 坐标系下二次可微"
    },
    {
        "id": 53,
        "name": "d'Alembertian 的定义",
        "math_expression": {
        "differential_form": "\Box \phi = \frac{1}{c^2} \frac{\partial^2 \phi}{\partial t^2} - \nabla^2 \phi"
        },
        "variables": [
        {"symbol": "\phi", "meaning": "标量场", "unit": "根据具体情况"},
        {"symbol": "c", "meaning": "光速", "unit": "m/s"},
        {"symbol": "\Box \phi", "meaning": "标量场的 d'Alembertian", "unit": "根据具体情况"}
        ],
        "keywords": ["d'Alembertian", "达朗贝尔算子", "Relativistic Electrodynamics"],
        "constraints": "标量场 \(\phi\) 在时间和空间坐标下二次可微，且光速 \(c\) 为常数"
    },
    {
        "id": 54,
        "name": "矢量场的 d'Alembertian 表达式",
        "math_expression": {
        "differential_form": "\Box \mathbf{A} = \frac{1}{c^2} \frac{\partial^2 \mathbf{A}}{\partial t^2} - \nabla^2 \mathbf{A}"
        },
        "variables": [
        {"symbol": "\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "c", "meaning": "光速", "unit": "m/s"},
        {"symbol": "\Box \mathbf{A}", "meaning": "矢量场的 d'Alembertian", "unit": "根据具体情况"}
        ],
        "keywords": ["矢量 d'Alembertian", "Relativistic Electrodynamics", "波动方程"],
        "constraints": "矢量场 \(\mathbf{A}\) 在时间和空间坐标下二次可微，且光速 \(c\) 为常数"
    },
    {
      "id": 55,
      "name": "电荷守恒定律（连续方程）",
      "math_expression": {
        "differential_form": "\\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot \\mathbf{J} = 0"
      },
      "variables": [
        {"symbol": "\\rho", "meaning": "密度电荷", "unit": "C/m³"},
        {"symbol": "\\mathbf{J}", "meaning": "电流密度", "unit": "A/m²"}
      ],
      "keywords": ["电荷守恒", "连续方程"],
      "constraints": "适用于电荷在空间中连续分布的情况"
    },
    {
      "id": 56,
      "name": "电磁场的应力张量",
      "math_expression": {
        "differential_form": "T_{ij} = \\varepsilon_0 \\left[ \\mathbf{E}_i \\mathbf{E}_j + c^2 \\mathbf{B}_i \\mathbf{B}_j - \\frac{1}{2} (\\mathbf{E} \\cdot \\mathbf{E} + c^2 \\mathbf{B} \\cdot \\mathbf{B}) \\delta_{ij} \\right]"
      },
      "variables": [
        {"symbol": "T_{ij}", "meaning": "应力张量分量", "unit": "N/m²"},
        {"symbol": "\\varepsilon_0", "meaning": "真空介电常数", "unit": "F/m"},
        {"symbol": "\\mathbf{E}", "meaning": "电场强度", "unit": "V/m"},
        {"symbol": "\\mathbf{B}", "meaning": "磁场强度", "unit": "T"},
        {"symbol": "c", "meaning": "光速", "unit": "m/s"},
        {"symbol": "\\delta_{ij}", "meaning": "Kronecker delta", "unit": "无单位"}
      ],
      "keywords": ["应力张量", "电磁场", "电场", "磁场"],
      "constraints": "适用于描述电磁场在介质中的应力分布"
    },
{
      "id": 57,
      "name": "柱坐标系下的散度",
      "math_expression": {
        "cylindrical_form": "\\nabla \\cdot \\mathbf{A} = \\frac{1}{\\rho} \\frac{\\partial}{\\partial \\rho} (\\rho A_\\rho) + \\frac{1}{\\rho} \\frac{\\partial A_\\phi}{\\partial \\phi} + \\frac{\\partial A_z}{\\partial z}"
      },
      "variables": [
        {"symbol": "\\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "\\rho", "meaning": "柱坐标系下的径向距离", "unit": "m"},
        {"symbol": "A_\\rho", "meaning": "矢量场在径向的分量", "unit": "根据具体情况"},
        {"symbol": "A_\\phi", "meaning": "矢量场在方位角方向的分量", "unit": "根据具体情况"},
        {"symbol": "A_z", "meaning": "矢量场在轴向的分量", "unit": "根据具体情况"}
      ],
      "keywords": ["散度", "柱坐标系"],
      "constraints": "适用于柱坐标系下的矢量场"
    },
    {
      "id": 58,
      "name": "柱坐标系下的旋度",
      "math_expression": {
        "cylindrical_form": "\\nabla \\times \\mathbf{A} = \\frac{1}{\\rho} \\left( \\frac{\\partial A_z}{\\partial \\phi} - \\frac{\\partial A_\\phi}{\\partial z} \\right) \\mathbf{e}_\\rho + \\frac{1}{\\rho} \\left( \\frac{\\partial A_\\rho}{\\partial z} - \\frac{\\partial A_z}{\\partial \\rho} \\right) \\mathbf{e}_\\phi + \\frac{1}{\\rho} \\frac{\\partial A_\\phi}{\\partial \\rho} \\mathbf{e}_z"
      },
      "variables": [
        {"symbol": "\\mathbf{A}", "meaning": "矢量场", "unit": "根据具体情况"},
        {"symbol": "\\rho", "meaning": "柱坐标系下的径向距离", "unit": "m"},
        {"symbol": "A_\\rho", "meaning": "矢量场在径向的分量", "unit": "根据具体情况"},
        {"symbol": "A_\\phi", "meaning": "矢量场在方位角方向的分量", "unit": "根据具体情况"},
        {"symbol": "A_z", "meaning": "矢量场在轴向的分量", "unit": "根据具体情况"}
      ],
      "keywords": ["旋度", "柱坐标系"],
      "constraints": "适用于柱坐标系下的矢量场"
    },
    {
      "id": 59,
      "name": "柱坐标系下的梯度",
      "math_expression": {
        "cylindrical_form": "\\nabla \\phi = \\frac{\\partial \\phi}{\\partial \\rho} \\mathbf{e}_\\rho + \\frac{1}{\\rho} \\frac{\\partial \\phi}{\\partial \\phi} \\mathbf{e}_\\phi + \\frac{\\partial \\phi}{\\partial z} \\mathbf{e}_z"
      },
      "variables": [
        {"symbol": "\\phi", "meaning": "标量场", "unit": "根据具体情况"},
        {"symbol": "\\rho", "meaning": "柱坐标系下的径向距离", "unit": "m"}
      ],
      "keywords": ["梯度", "柱坐标系"],
      "constraints": "适用于柱坐标系下的标量场"
    },
    {
      "id": 60,
      "name": "Neumann边界条件下的电势求解",
      "math_expression": {
        "neumann_form": "\\phi(\\mathbf{r}) = \\int G(\\mathbf{r},\\mathbf{r}')\\rho(\\mathbf{r}')d\\tau' + \\oint_S \\left[\\phi(\\mathbf{r}')p(\\mathbf{r}')\\nabla'G(\\mathbf{r},\\mathbf{r}') - G(\\mathbf{r},\\mathbf{r}')p(\\mathbf{r}')\\nabla'\\phi(\\mathbf{r}')\\right] \\cdot d\\mathbf{S}'"
      },
      "variables": [
        {"symbol": "\\phi", "meaning": "电势", "unit": "V"},
        {"symbol": "\\mathbf{r}", "meaning": "位置矢量", "unit": "m"},
        {"symbol": "\\mathbf{r}'", "meaning": "源位置矢量", "unit": "m"},
        {"symbol": "\\rho", "meaning": "电荷密度", "unit": "C/m³"},
        {"symbol": "G", "meaning": "Green函数", "unit": ""},
        {"symbol": "p", "meaning": "边界上的函数", "unit": ""}
      ],
      "keywords": ["Neumann边界条件", "电势", "Green函数"],
      "constraints": "适用于边界上给定电势法向导数的情况"
    },
    {
      "id": 61,
      "name": "Dirichlet边界条件下的电势求解",
      "math_expression": {
        "dirichlet_form": "\\phi(\\mathbf{r}) = \\int G_D(\\mathbf{r},\\mathbf{r}')\\rho(\\mathbf{r}')d\\tau' + \\oint_S \\phi(\\mathbf{r}')p(\\mathbf{r}')\\nabla'G_D(\\mathbf{r},\\mathbf{r}') \\cdot d\\mathbf{S}'"
      },
      "variables": [
        {"symbol": "\\phi", "meaning": "电势", "unit": "V"},
        {"symbol": "\\mathbf{r}", "meaning": "位置矢量", "unit": "m"},
        {"symbol": "\\mathbf{r}'", "meaning": "源位置矢量", "unit": "m"},
        {"symbol": "\\rho", "meaning": "电荷密度", "unit": "C/m³"},
        {"symbol": "G_D", "meaning": "Dirichlet Green函数", "unit": ""},
        {"symbol": "p", "meaning": "边界上的函数", "unit": ""}
      ],
      "keywords": ["Dirichlet边界条件", "电势", "Green函数"],
      "constraints": "适用于边界上给定电势的情况"
      },
  {
    "id": 62,
    "name": "均匀静电场中介质球的电势解",
    "math_expression": {
      "potential_solution": "\\Phi_{\\text{in}}(\\mathbf{x}) = -\\left(\\frac{3\\epsilon_2}{\\epsilon_1 + 2\\epsilon_2}\\right) E_0 r \\cos\\theta \\\\ \\Phi_{\\text{out}}(\\mathbf{x}) = -E_0 r \\cos\\theta + \\left(\\frac{\\epsilon_1 - \\epsilon_2}{\\epsilon_1 + 2\\epsilon_2}\\right) E_0 \\frac{a^3}{r^2} \\cos\\theta"
    },
    "variables": [
      {"symbol": "\\Phi_{\\text{in}}", "meaning": "介质球内部电势", "unit": "V"},
      {"symbol": "\\Phi_{\\text{out}}", "meaning": "介质球外部电势", "unit": "V"},
      {"symbol": "E_0", "meaning": "外加均匀电场强度", "unit": "V/m"},
      {"symbol": "r", "meaning": "径向距离（球坐标系）", "unit": "m"},
      {"symbol": "a", "meaning": "介质球半径", "unit": "m"},
      {"symbol": "\\theta", "meaning": "极角（球坐标系）", "unit": "rad"},
      {"symbol": "\\epsilon_1", "meaning": "介质球内部介电常数", "unit": "F/m"},
      {"symbol": "\\epsilon_2", "meaning": "外部介质介电常数", "unit": "F/m"}
    ],
    "keywords": ["介质球", "均匀电场", "电势", "拉普拉斯方程", "边界条件"],
    "constraints": "适用于球形对称介质球在均匀电场中的静电平衡情况，满足内部与外部电势连续性及法向电场边界条件"
  },
  {
    "id": 63,
    "name": "电偶极子间的相互作用能",
    "math_expression": {
    "formula": "U = \frac{1}{4\pi\epsilon_0} \left[ \frac{\mathbf{p}_1 \cdot \mathbf{p}_2 - 3(\mathbf{n} \cdot \mathbf{p}_1)(\mathbf{n} \cdot \mathbf{p}_2)}{|\mathbf{x}_1 - \mathbf{x}_2|^3} + \frac{4\pi}{3}(\mathbf{p}_1 \cdot \mathbf{p}_2) \delta^{(3)}(\mathbf{x}_1 - \mathbf{x}_2) \right]"
    },
    "variables": [
    {"symbol": "\mathbf{p}_1", "meaning": "第一个电偶极子的偶极矩", "unit": "C·m"},
    {"symbol": "\mathbf{p}_2", "meaning": "第二个电偶极子的偶极矩", "unit": "C·m"},
    {"symbol": "\mathbf{x}_1", "meaning": "第一个电偶极子的位置向量", "unit": "m"},
    {"symbol": "\mathbf{x}_2", "meaning": "第二个电偶极子的位置向量", "unit": "m"},
    {"symbol": "\mathbf{n}", "meaning": "从\mathbf{x}_1指向\mathbf{x}_2的单位向量", "unit": "无量纲"},
    {"symbol": "\epsilon_0", "meaning": "真空介电常数", "unit": "F/m"},
    {"symbol": "\delta^{(3)}", "meaning": "三维狄拉克δ函数", "unit": "1/m³"}
    ],
    "keywords": ["电偶极子", "相互作用能", "δ函数"],
    "constraints": "适用于点电偶极子的情况，当两个偶极子位置重合时存在自能项"
  },
  {
    "id": 64,
    "name": "轨道磁矩（经典理论）",
    "math_expression": {
      "formula": "\\mathbf{m} = \\frac{q}{2m} \\mathbf{L}"
    },
    "variables": [
      {
        "symbol": "q",
        "meaning": "电荷量",
        "unit": "库仑（C）"
      },
      {
        "symbol": "m",
        "meaning": "带电粒子质量",
        "unit": "千克（kg）"
      },
      {
        "symbol": "\\mathbf{L}",
        "meaning": "角动量",
        "unit": "kg·m²/s"
      }
    ],
    "keywords": ["轨道磁矩", "经典理论"],
    "constraints": "适用于带电粒子（如电子）的轨道运动，例如原子中的电子绕核运动。"
  },
  {
    "id": 65,
    "name": "自旋磁矩（量子理论）",
    "math_expression": {
      "formula": "\\mathbf{m} = g \\cdot \\frac{q}{2m} \\mathbf{S}"
    },
    "variables": [
      {
        "symbol": "\\mathbf{S}",
        "meaning": "自旋角动量",
        "unit": "kg·m²/s"
      },
      {
        "symbol": "g",
        "meaning": "朗德因子（电子自旋 g ≈ 2.0023）",
        "unit": "无量纲"
      }
    ],
    "keywords": ["自旋磁矩", "量子理论"],
    "constraints": "量子力学中自旋磁矩与经典轨道磁矩的差异由 g-因子体现。"
  },
  {
    "id": 66,
    "name": "磁矩的势能",
    "math_expression": {
      "formula": "U = -\\mathbf{m} \\cdot \\mathbf{B}"
    },
    "variables": [
      {
        "symbol": "\\mathbf{B}",
        "meaning": "外磁场",
        "unit": "特斯拉(T)"
      },
      {
        "symbol": "U",
        "meaning": "势能",
        "unit": "焦耳（J）"
      }
    ],
    "keywords": ["磁矩", "势能"],
    "constraints": "磁矩趋向于与外磁场方向对齐以最小化势能。"
  },
  {
  "id": 67,
  "name": "回磁比（Gyromagnetic Ratio）",
  "math_expression": {
    "formula": "γ = \\frac{\\mathbf{m}}{\\mathbf{L}} = \\frac{q}{2m}"
  },
  "keywords": ["回磁比", "Gyromagnetic Ratio"],
  "constraints": "经典回磁比为常数，量子力学中需引入 g-因子修正。"
  }, 



  ]
}
# 差三个公式：球坐标系、柱坐标系、直角坐标系下laplace方程的解