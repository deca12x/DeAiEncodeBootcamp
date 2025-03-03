# Exercise 1: Create a Fungible Token with OpenZeppelin

In this exercise, you will create your first ERC20 token using the OpenZeppelin Wizard and prepare it for deployment.

## Objective

Create a custom ERC20 token with specific features using the OpenZeppelin Wizard.

## Prerequisites

- Web browser
- [MetaMask](https://metamask.io/) wallet installed and configured for Sepolia testnet
- Basic understanding of ERC20 tokens

## Steps

1. Visit the [OpenZeppelin Wizard](https://wizard.openzeppelin.com/)

2. Configure your token:

   ```solidity
   // Token Configuration
   name: "MyAIToken"
   symbol: "AIT"
   premint: 1000000
   ```

3. Add the following features:
   - [x] Mintable (allows creating more tokens)
   - [x] Burnable (allows destroying tokens)
   - [x] Pausable (allows pausing transfers)
   - [x] Permit (enables gasless approvals)

4. Review the generated code:

   ```solidity
   // SPDX-License-Identifier: MIT
   pragma solidity ^0.8.20;

   import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
   import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
   import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
   import "@openzeppelin/contracts/access/Ownable.sol";
   import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";

   contract MyAIToken is ERC20, ERC20Burnable, ERC20Pausable, Ownable, ERC20Permit {
       constructor(address initialOwner)
           ERC20("MyAIToken", "AIT")
           Ownable(initialOwner)
           ERC20Permit("MyAIToken")
       {
           _mint(msg.sender, 1000000 * 10 ** decimals());
       }

       function pause() public onlyOwner {
           _pause();
       }

       function unpause() public onlyOwner {
           _unpause();
       }

       function mint(address to, uint256 amount) public onlyOwner {
           _mint(to, amount);
       }

       // The following function is needed to comply with the pausable extension
       function _update(address from, address to, uint256 value)
           internal
           override(ERC20, ERC20Pausable)
       {
           super._update(from, to, value);
       }
   }
   ```

5. Copy the generated code for use in the next exercise

## Expected Output

- A complete Solidity smart contract for an ERC20 token
- Contract includes all specified features (mintable, burnable, pausable, permit)
- Contract is ready for deployment

## Verification

Your contract should:

- [x] Have the correct name and symbol
- [x] Include all specified features
- [x] Have a premint amount of 1,000,000 tokens
- [x] Compile without errors in Remix IDE

## Common Issues

1. **Wrong Solidity Version**
   - Ensure your Solidity version matches the imports (^0.8.20)
   - Update the pragma line if needed

2. **Missing Imports**
   - All OpenZeppelin imports should be present
   - Check for any typos in import paths

3. **Constructor Parameters**
   - Make sure the constructor includes the initialOwner parameter
   - Verify the token name and symbol match your configuration

## Additional Resources

- [OpenZeppelin Contracts Documentation](https://docs.openzeppelin.com/contracts/4.x/)
- [ERC20 Token Standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)
- [Understanding Smart Contract Inheritance](https://docs.openzeppelin.com/contracts/4.x/extending-contracts)
