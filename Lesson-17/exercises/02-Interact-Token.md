# Exercise 3: Interact with Deployed Token

In this exercise, you will learn how to interact with your deployed ERC20 token using both Remix IDE and Etherscan.

## Objective

Learn how to perform various token operations including transfers, minting, burning, and managing token permissions.

## Prerequisites

- Completed Exercises 1 and 2
- Deployed and verified token contract
- Access to contract address and owner wallet

## Steps

1. Interact via Remix IDE:

   ```solidity
   // Load your contract
   Contract Address: <your-contract-address>
   ```

2. Basic token operations:
   - Check your balance:

     ```solidity
     // Call balanceOf function
     balanceOf(<your-wallet-address>)
     ```

   - Transfer tokens:

     ```solidity
     // Transfer 100 tokens
     transfer(<recipient-address>, 100000000000000000000) // 100 tokens with 18 decimals
     ```

3. Owner-only operations:
   - Mint new tokens:

     ```solidity
     // Mint 500 tokens to an address
     mint(<recipient-address>, 500000000000000000000)
     ```

   - Pause/Unpause transfers:

     ```solidity
     // Pause all transfers
     pause()
     
     // Unpause transfers
     unpause()
     ```

4. Token burning:

   ```solidity
   // Burn 50 tokens from your balance
   burn(50000000000000000000)
   ```

5. Advanced operations:
   - Approve spending:

     ```solidity
     // Approve address to spend 200 tokens
     approve(<spender-address>, 200000000000000000000)
     ```

   - Check allowance:

     ```solidity
     // Check approved amount
     allowance(<owner-address>, <spender-address>)
     ```

## Expected Output

For each operation, you should see:

- Transaction confirmation in MetaMask
- Updated balances and states
- Transaction history in Etherscan

## Verification

Verify the following:

- [x] Token transfers are successful
- [x] Minting increases total supply
- [x] Burning decreases total supply
- [x] Pause/Unpause affects transfer ability
- [x] Approvals are correctly recorded

## Common Issues

1. **Insufficient Balance**
   - Check token balance before transfer
   - Verify decimal places (18 decimals standard)

2. **Permission Errors**
   - Ensure you're using the owner wallet for restricted functions
   - Verify approved amounts for transfers

3. **Failed Transactions**
   - Check if contract is paused
   - Verify gas limits and prices
   - Confirm recipient addresses are valid

## Additional Resources

- [ERC20 Interface Documentation](https://docs.openzeppelin.com/contracts/4.x/api/token/erc20)
- [Understanding Token Decimals](https://docs.openzeppelin.com/contracts/4.x/erc20#a-note-on-decimals)
- [MetaMask Transaction Guide](https://support.metamask.io/hc/en-us/articles/360015488931-How-to-send-tokens)
