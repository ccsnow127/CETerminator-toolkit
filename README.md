# CETerminator
<p align="center">
    <br>
    <img src="Learn_Illustration_What_is_a_Smart_Contract__1_.png" width="300"/>
    <br>
</p>

CETerminator is an automated tool designed to detect and rectify NatSpec comment errors in Ethereum smart contracts. By enhancing adherence to NatSpec standards, CETerminator aims to improve code clarity and reduce financial risks associated with misunderstandings in smart contract functionalities.

## Overview

NatSpec comments are essential in smart contracts for providing clear and informative documentation. They help users gain an accurate understanding of contract behavior, thus diminishing financial risk. However, widespread non-adherence to NatSpec standards causes confusion among end-users and developers.

CETerminator addresses this issue by:

- **Empirical Analysis**: Conducted the first empirical study on 253 verified contracts encompassing 16,620 functions from Etherscan.
- **Error Identification**: Found that **87%** of smart contract functions have NatSpec comment errors.
- **Pattern Recognition**: Pinpointed prevalent error patterns in existing NatSpec comments.

## Features

- **Automated Detection**: Identifies missing or incorrect NatSpec comments in smart contracts.
- **In-Context Learning**: Utilizes large language models to generate accurate NatSpec comments.
- **Heuristic Correction**: Applies corpus-driven heuristic rules to correct diverse error categories.
- **Performance Metrics**: Demonstrates high token overlap rates and significant improvements in precision, recall, and F1-scores over existing methods.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/CETerminator.git

# Navigate to the directory
cd CETerminator

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run CETerminator on your smart contract file
python ceterminator.py --input your_contract.sol --output corrected_contract.sol
```

## Evaluation Results

CETerminator has shown impressive results in evaluations:

- **Missing Comment Errors**: Achieved a high token overlap rate in addressing missing comments.
- **Inconsistency Comment Errors**:
  - Precision: **85.28%**
  - Recall: **86.48%**
  - F1-Score: **85.85%**
- Outperformed the baseline methods by approximately **40%** in all metrics.

## Example

### Before Correction

```solidity
// Missing NatSpec comments
function transfer(address _to, uint256 _value) public returns (bool success) {
    // Function implementation
}
```

### After Correction with CETerminator

```solidity
/// @notice Transfers tokens to a specified address
/// @param _to The address to transfer tokens to
/// @param _value The amount of tokens to be transferred
/// @return success A boolean value indicating whether the operation succeeded
function transfer(address _to, uint256 _value) public returns (bool success) {
    // Function implementation
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).
