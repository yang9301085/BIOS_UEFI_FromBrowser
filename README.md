# UEFI Form Browser 项目

## 项目描述
此项目用于实现 UEFI Form Browser，这是 UEFI 固件中的一个核心组件，用于在固件启动过程中提供用户界面，允许用户配置 BIOS/UEFI 设置。

Form Browser 基于 UEFI HII (Human Interface Infrastructure) 框架，使用 IFR (Internal Forms Representation) 语言定义表单，并通过 EFI_FORM_BROWSER2_PROTOCOL 提供界面交互功能。

## 项目结构
- **edk2/**: UEFI EDK2 代码库，包含构建 UEFI 固件所需的核心组件
  - **MdePkg/**: 核心包，包含基础 UEFI 协议定义
  - **MdeModulePkg/**: 模块包，包含标准 UEFI 模块实现
  - **CustomFormBrowserPkg/**: 自定义 Form Browser 包
    - **Include/Library/**: 库头文件
    - **Library/CustomFormBrowserLib/**: 自定义 Form Browser 库实现
    - **Application/CustomFormBrowserApp/**: 自定义 Form Browser 应用程序

## 技术实现

### 核心组件
1. **CustomFormBrowserLib**
   - 提供简化的 Form Browser 接口
   - 支持创建和显示表单
   - 封装了复杂的 HII 和 IFR 操作

2. **CustomFormBrowserApp**
   - 基于 CustomFormBrowserLib 的示例应用程序
   - 演示如何使用库创建和显示表单
   - 提供基本的用户交互功能

### 关键技术
- **EFI_FORM_BROWSER2_PROTOCOL**: 提供 Form Browser 核心功能
- **HII 框架**: 用于管理用户界面资源
- **IFR 语言**: 用于定义表单结构
- **UEFI 驱动模型**: 用于实现和部署组件

## 构建指南

### 环境要求
- Linux 或 Windows 操作系统
- Python 3.x
- UEFI 工具链 (GCC, CLANG 等)

### 构建步骤
1. 初始化子模块
   ```bash
   git submodule update --init --recursive
   ```

2. 安装依赖
   ```bash
   pip install -r edk2/pip-requirements.txt
   ```

3. 设置构建环境
   ```bash
   cd edk2
   source edksetup.sh
   ```

4. 构建 CustomFormBrowserPkg
   ```bash
   build -p CustomFormBrowserPkg/CustomFormBrowserPkg.dsc -t GCC5
   ```

## 测试方法

### 在 UEFI 环境中测试
1. 将构建生成的 `.efi` 文件复制到 UEFI 可访问的存储设备
2. 在 UEFI Shell 中运行应用程序
   ```
   CustomFormBrowserApp.efi
   ```

### 功能测试
- 验证表单显示是否正确
- 测试用户输入和导航功能
- 检查设置值的保存和恢复

## 相关文档

### 技术参考
- [UEFI Specification](https://uefi.org/specifications)
- [EDK2 Documentation](https://github.com/tianocore/tianocore.github.io/wiki/EDK-II)
- [HII Specification](https://uefi.org/specifications/UEFI/2.10/12_Human_Interface_Infrastructure.html)

### 代码参考
- **FormBrowser2.h**: `/edk2/MdePkg/Include/Protocol/FormBrowser2.h`
- **SetupBrowserDxe**: `/edk2/MdeModulePkg/Universal/SetupBrowserDxe/`

## 未来计划

1. **功能增强**
   - 支持更多表单控件类型
   - 实现更丰富的用户界面元素
   - 添加主题和样式支持

2. **平台兼容性**
   - 测试在不同 UEFI 平台上的兼容性
   - 优化不同分辨率和显示模式的支持

3. **性能优化**
   - 减少内存占用
   - 提高表单加载和渲染速度

4. **文档完善**
   - 编写详细的 API 文档
   - 提供更多使用示例和教程

## 贡献指南

欢迎贡献代码、报告问题或提出建议。请确保遵循 UEFI EDK2 的代码风格和贡献规范。

## 许可证

此项目基于 UEFI EDK2 的许可证，详情请参考 `edk2/LICENSE` 文件。