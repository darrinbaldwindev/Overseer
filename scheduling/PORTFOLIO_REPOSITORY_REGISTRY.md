# Portfolio Repository Registry

Last reconciled: 2026-08-27

## Accessible portfolio

| Repository | Role | Scheduler tier |
|---|---|---|
| AgentOS | Future native control plane | P0 / continuous control-plane attention |
| Overseer | GPTChat Repo Overseer + GPTChat Overseer control infrastructure | P0 / continuous control-plane attention |
| Franchise | Franchise platform/business | P1 active |
| GlobalShopCo | Ecommerce/business platform | P1 active |
| GlobalShopCo-Headless | Headless storefront implementation | P1 active/dependent on GlobalShopCo |
| GemVerse | Product/project repository | P2 adaptive |
| MyPrimeDelivery | Delivery project | P2 adaptive |
| PRS | New/early project | P3 adaptive until activity/priority increases |
| GhostKitchen | New/early project | P3 adaptive until activity/priority increases |

## Scheduling policy
This registry is not a fixed permanent priority list. GPTChat Overseer should re-rank based on health, activity, dependencies, milestones, failures and owner priorities.

## Control-plane rule
Overseer and AgentOS receive elevated monitoring because improvements there can unblock the entire portfolio.

## Dependency rule
GlobalShopCo-Headless should be scheduled with awareness of GlobalShopCo milestones. AgentOS/Overseer scheduler work should be prioritised when it can materially improve autonomy across multiple projects.

## Future repositories
New repositories must be added automatically during portfolio reconciliation and assigned an initial adaptive tier based on activity and risk.
