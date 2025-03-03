# Exercise 2: Deploy Token to Sepolia Testnet

In this exercise, you will deploy your ERC20 token to the Sepolia testnet using Remix IDE and MetaMask.

## Objective

Deploy the ERC20 token created in Exercise 1 to the Sepolia testnet and verify it on Etherscan.

## Prerequisites

- Completed Exercise 1
- [MetaMask](https://metamask.io/) wallet with Sepolia test ETH
- [Remix IDE](https://remix.ethereum.org/) open in your browser
- [Sepolia Etherscan](https://sepolia.etherscan.io/) account (for verification)

## Steps

1. Open Remix IDE and create a new file

2. Paste the code from Exercise 1 into the file

3. Configure the Remix environment:
   - Click the "Solidity Compiler" tab
   - Select compiler version 0.8.20
   - Enable optimization
   - Click "Compile MyAIToken.sol"

4. Deploy the contract:
   - Click the "Deploy & Run Transactions" tab
   - Environment: Select "Injected Provider - MetaMask"
   - Account: Your MetaMask account should appear
   - Contract: Select "MyAIToken"
   - Deploy parameters: Enter your wallet address as `initialOwner`

5. Confirm deployment:
   - MetaMask will pop up
   - Review the gas fees
   - Confirm the transaction
   - Wait for deployment to complete

6. Verify the contract on Sepolia Etherscan:
   - Copy the deployed contract address
   - Visit [Sepolia Etherscan](https://sepolia.etherscan.io/)
   - Paste the contract address in the search bar
   - Click "Verify and Publish"
   - Select "Solidity (Single file)"
   - Enter the contract details:
     - Compiler Version: 0.8.20
     - Open Source License: MIT
   - Paste the contract code
   - Submit for verification

## Expected Output

- Successfully deployed contract on Sepolia testnet
- Contract verified on Sepolia Etherscan
- Ability to view token details and transactions

## Verification

Your deployment should:

- [x] Show successful transaction confirmation
- [x] Display contract address on Sepolia network
- [x] Be verified on Sepolia Etherscan
- [x] Show correct token supply and owner address

## Common Issues

1. **Insufficient Gas**
   - Ensure you have enough Sepolia ETH
   - Try adjusting gas price if transaction fails

2. **MetaMask Connection**
   - Verify MetaMask is connected to Sepolia
   - Check if the correct account is selected

3. **Verification Failures**
   - Double-check compiler version
   - Ensure all contract code is included
   - Verify constructor arguments are correct

## Additional Resources

- [Remix IDE Documentation](https://remix-ide.readthedocs.io/en/latest/)
- [MetaMask Documentation](https://docs.metamask.io/)
- [Etherscan Verification Guide](https://docs.etherscan.io/tutorials/verifying-contracts-programmatically)
