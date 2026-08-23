# Discovery Layer

The discovery layer will provide deterministic GitHub inventory and repository snapshot operations to the Manus Overseer runtime.

Responsibilities:

1. Discover accessible repositories.
2. Normalize repository metadata.
3. Detect portfolio changes.
4. Capture exact refs for scans.
5. Report access limitations.

Discovery must not assume the current portfolio is fixed.
