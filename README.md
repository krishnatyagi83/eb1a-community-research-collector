# EB-1A Community Research Collector

> **Status: approval pending.** This repository documents a proposed personal, non-commercial, read-only research tool. It will not access Reddit's API unless and until Reddit grants explicit approval for the described use case.

## Purpose

The proposed tool would help one individual review public discussions in r/eb_1a while preserving each submission's complete public reply context. Reddit posts and comments would be treated as anecdotal community reports and research leads—not as legal authority, legal advice, or evidence that a particular argument caused an immigration outcome.

## Requested scope

- Community: r/eb_1a only
- Date window: April 25, 2026 through July 25, 2026
- Content: public submissions and their complete public comment trees, including nested replies
- Users: one applicant; no external customers or public audience
- Access: one approved OAuth client with a descriptive User-Agent
- Actions: read-only; no posting, commenting, voting, messaging, moderation, or private-area access

## Planned processing

1. Retrieve submissions in the approved community and date window.
2. Retrieve each submission's public comments and nested replies.
3. Preserve source identifiers, parent-child relationships, permalinks, and timestamps.
4. Create a private local index for personal review.
5. Reconcile the stored records against current Reddit data and remove deleted content and associated derived records.

## Data and privacy controls

- No user profiling, sensitive-trait inference, re-identification, or matching to off-platform identities.
- No sale, licensing, public redistribution, advertising, or commercial use.
- No machine-learning model training or fine-tuning.
- Credentials will be supplied through local environment variables and will never be committed.
- Data will be retained locally only as necessary for the approved review.
- Deleted submissions, comments, deleted-account identifiers, summaries, and search indexes derived from removed material will be deleted during reconciliation.
- Rate-limit response headers will be honored; limits will not be bypassed or distributed across multiple accounts or clients.

## AI-assisted review request

The API-access request asks Reddit to clarify whether selected retrieved text may be processed through OpenAI Codex for private, ad hoc summarization and semantic retrieval. This would be inference only, not model training or fine-tuning. If Reddit does not explicitly permit that third-party processing, the tool will be limited to local collection and manual review, and Reddit data will not be sent to an external AI provider.

## Implementation status

The repository is intentionally non-operational while approval is pending. A safe placeholder script records the proposed scope and refuses network access unless an explicit approval flag is present. OAuth credentials, API calls, storage, summarization, and deletion synchronization will be implemented only within the scope Reddit approves.

## Non-affiliation

This is an independent personal research project. It is not affiliated with, sponsored by, or endorsed by Reddit, USCIS, or any law firm. Counsel should review any immigration-related conclusions against current primary authority.
