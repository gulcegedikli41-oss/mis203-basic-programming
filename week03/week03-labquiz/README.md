# Lab Quiz - Week 03: Order Approval Policy

## Test
*Limitiation values were tested, and price was removed for refused orders.*

## Boundary Test Table
| order_amount | available_stock | requested_quantity | member_status | Expected Output |
| :---: | :---: | :---: | :---: | :--- |
| 499.00 | 10 | 2 | "true" | Approved (no discount) - 499.00 TRY |
| 500.00 | 10 | 2 | "true" | Approved (10% discount) - 450.00 TRY |
| 501.00 | 10 | 2 | "true" | Approved (10% discount) - 450.90 TRY |
| 600.00 | 2 | 5 | "true" | Rejected (invalid quantity/stock) |

