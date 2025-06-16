from dataclasses import dataclass
from enum import StrEnum


@dataclass
class PullRequestUser:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: bool


@dataclass
class PullRequestLinks:
    url: str
    html_url: str
    diff_url: str
    patch_url: str
    merged_at: str | None


@dataclass
class Reactions:
    url: str
    total_count: int
    plus_one: int
    minus_one: int
    laugh: int
    hooray: int
    confused: int
    heart: int
    rocket: int
    eyes: int


@dataclass
class PullRequest:
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    user: PullRequestUser
    labels: list
    state: str
    locked: bool
    assignee: None
    assignees: list
    milestone: None
    comments: int
    created_at: str
    updated_at: str
    closed_at: str | None
    author_association: str
    type: str | None
    active_lock_reason: str | None
    draft: bool
    pull_request: PullRequestLinks
    body: str
    reactions: Reactions
    timeline_url: str
    performed_via_github_app: None
    state_reason: str | None
    score: float

    @classmethod
    def from_dict(cls, data: dict) -> "PullRequest":
        user = PullRequestUser(**data["user"])
        pr_links = PullRequestLinks(**data["pull_request"])
        reactions_raw = data.get("reactions", {})
        reactions = Reactions(
            url=reactions_raw.get("url", ""),
            total_count=reactions_raw.get("total_count", 0),
            plus_one=reactions_raw.get("+1", 0),
            minus_one=reactions_raw.get("-1", 0),
            laugh=reactions_raw.get("laugh", 0),
            hooray=reactions_raw.get("hooray", 0),
            confused=reactions_raw.get("confused", 0),
            heart=reactions_raw.get("heart", 0),
            rocket=reactions_raw.get("rocket", 0),
            eyes=reactions_raw.get("eyes", 0),
        )

        return cls(
            url=data["url"],
            repository_url=data["repository_url"],
            labels_url=data["labels_url"],
            comments_url=data["comments_url"],
            events_url=data["events_url"],
            html_url=data["html_url"],
            id=data["id"],
            node_id=data["node_id"],
            number=data["number"],
            title=data["title"],
            user=user,
            labels=data["labels"],
            state=data["state"],
            locked=data["locked"],
            assignee=None,
            assignees=data["assignees"],
            milestone=None,
            comments=data["comments"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            closed_at=data.get("closed_at"),
            author_association=data["author_association"],
            type=data.get("type"),
            active_lock_reason=data.get("active_lock_reason"),
            draft=data["draft"],
            pull_request=pr_links,
            body=data.get("body", ""),
            reactions=reactions,
            timeline_url=data["timeline_url"],
            performed_via_github_app=None,
            state_reason=data.get("state_reason"),
            score=data["score"],
        )


@dataclass
class GitHubPlan:
    collaborators: int
    name: str
    space: int
    private_repos: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            collaborators=data.get("collaborators", 0),
            name=data.get("name", ""),
            space=data.get("space", 0),
            private_repos=data.get("private_repos", 0),
        )


@dataclass
class GitHubUser:
    login: str | None
    id: int | None
    user_view_type: str | None
    node_id: str | None
    avatar_url: str | None
    gravatar_id: str | None
    url: str | None
    html_url: str | None
    followers_url: str | None
    following_url: str | None
    gists_url: str | None
    starred_url: str | None
    subscriptions_url: str | None
    organizations_url: str | None
    repos_url: str | None
    events_url: str | None
    received_events_url: str | None
    type: str | None
    site_admin: bool | None
    name: str | None
    company: str | None
    blog: str | None
    location: str | None
    email: str | None
    notification_email: str | None
    hireable: bool | None
    bio: str | None
    twitter_username: str | None
    public_repos: int | None

    public_gists: int | None
    followers: int | None
    following: int | None
    created_at: str | None
    updated_at: str | None
    private_gists: int | None = None
    total_private_repos: int | None = None
    owned_private_repos: int | None = None
    disk_usage: int | None = None
    collaborators: int | None = None
    two_factor_authentication: bool | None = None
    business_plus: bool | None = None

    ldap_dn: str | None = None
    plan: GitHubPlan | None = None

    @classmethod
    def from_dict(cls, data: dict):
        plan = data.get("plan")
        return cls(
            login=data.get("login"),
            id=data.get("id"),
            user_view_type=data.get("user_view_type"),
            node_id=data.get("node_id"),
            avatar_url=data.get("avatar_url"),
            gravatar_id=data.get("gravatar_id"),
            url=data.get("url"),
            html_url=data.get("html_url"),
            followers_url=data.get("followers_url"),
            following_url=data.get("following_url"),
            gists_url=data.get("gists_url"),
            starred_url=data.get("starred_url"),
            subscriptions_url=data.get("subscriptions_url"),
            organizations_url=data.get("organizations_url"),
            repos_url=data.get("repos_url"),
            events_url=data.get("events_url"),
            received_events_url=data.get("received_events_url"),
            type=data.get("type"),
            site_admin=data.get("site_admin"),
            name=data.get("name"),
            company=data.get("company"),
            blog=data.get("blog"),
            location=data.get("location"),
            email=data.get("email"),
            notification_email=data.get("notification_email"),
            hireable=data.get("hireable"),
            bio=data.get("bio"),
            twitter_username=data.get("twitter_username"),
            public_repos=data.get("public_repos"),
            public_gists=data.get("public_gists"),
            followers=data.get("followers"),
            following=data.get("following"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            private_gists=data.get("private_gists"),
            total_private_repos=data.get("total_private_repos"),
            owned_private_repos=data.get("owned_private_repos"),
            disk_usage=data.get("disk_usage"),
            collaborators=data.get("collaborators"),
            two_factor_authentication=data.get("two_factor_authentication"),
            business_plus=data.get("business_plus"),
            ldap_dn=data.get("ldap_dn"),
            plan=GitHubPlan.from_dict(plan) if plan else None,
        )


class RepoType(StrEnum):
    ALL = "all"
    OWNER = "owner"
    MEMBER = "member"


@dataclass
class GitHubLicense:
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
class GitHubRepository:
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: GitHubUser
    html_url: str
    permissions: dict[str, bool] | None
    description: str | None
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str | None
    size: int
    stargazers_count: int
    watchers_count: int
    language: str | None
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: str | None
    archived: bool
    disabled: bool
    open_issues_count: int

    license: GitHubLicense | None
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    topics: list[str]
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            **{
                **data,
                "owner": GitHubUser.from_dict(data["owner"]),
                "license": GitHubLicense.from_dict(data["license"])
                if data.get("license")
                else None,
            }
        )


@dataclass
class GitHubLabel:
    id: int
    node_id: str
    url: str
    name: str
    color: str
    default: bool
    description: str


@dataclass
class GitHubIssueType:
    id: int
    node_id: str
    name: str
    description: str
    color: str
    created_at: str
    updated_at: str
    is_enabled: bool


@dataclass
class GitHubSubIssuesSummary:
    total: int
    completed: int
    percent_completed: int


@dataclass
class GitHubReactions:
    url: str
    total_count: int
    plus_one: int
    minus_one: int
    laugh: int

    hooray: int
    confused: int
    heart: int
    rocket: int
    eyes: int

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            url=d["url"],
            total_count=d["total_count"],
            plus_one=d.get("+1", 0),
            minus_one=d.get("-1", 0),
            laugh=d.get("laugh", 0),
            hooray=d.get("hooray", 0),
            confused=d.get("confused", 0),
            heart=d.get("heart", 0),
            rocket=d.get("rocket", 0),
            eyes=d.get("eyes", 0),
        )


@dataclass
class GitHubIssue:
    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    user: GitHubUser
    labels: list[GitHubLabel]
    state: str
    locked: bool
    assignee: None
    assignees: list
    milestone: None
    comments: int
    created_at: str
    updated_at: str
    closed_at: str | None
    author_association: str
    type: GitHubIssueType | None
    active_lock_reason: str | None
    sub_issues_summary: GitHubSubIssuesSummary
    body: str
    reactions: GitHubReactions
    timeline_url: str
    performed_via_github_app: None
    state_reason: str | None
    score: float

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            url=d["url"],
            repository_url=d["repository_url"],
            labels_url=d["labels_url"],
            comments_url=d["comments_url"],
            events_url=d["events_url"],
            html_url=d["html_url"],
            id=d["id"],
            node_id=d["node_id"],
            number=d["number"],
            title=d["title"],
            user=GitHubUser.from_dict(d["user"]),
            labels=[GitHubLabel(**label) for label in d["labels"]],
            state=d["state"],
            locked=d["locked"],
            assignee=None,
            assignees=d["assignees"],
            milestone=None,
            comments=d["comments"],
            created_at=d["created_at"],
            updated_at=d["updated_at"],
            closed_at=d.get("closed_at"),
            author_association=d["author_association"],
            type=GitHubIssueType(**d["type"]) if d.get("type") else None,
            active_lock_reason=d.get("active_lock_reason"),
            sub_issues_summary=GitHubSubIssuesSummary(**d["sub_issues_summary"]),
            body=d["body"],
            reactions=GitHubReactions.from_dict(d["reactions"]),
            timeline_url=d["timeline_url"],
            performed_via_github_app=None,
            state_reason=d.get("state_reason"),
            score=d["score"],
        )


@dataclass
class DetailedPullRequest:
    url: str

    id: int
    node_id: str
    html_url: str
    diff_url: str

    patch_url: str
    issue_url: str
    number: int
    state: str
    locked: bool
    title: str
    user: GitHubUser
    body: str | None
    created_at: str
    updated_at: str
    closed_at: str | None
    merged_at: str | None
    merge_commit_sha: str | None
    assignee: None
    assignees: list
    requested_reviewers: list
    requested_teams: list
    labels: list

    milestone: None

    draft: bool
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    author_association: str
    auto_merge: None
    active_lock_reason: str | None

    merged: bool
    mergeable: bool | None
    rebaseable: bool | None
    mergeable_state: str
    merged_by: GitHubUser | None
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            url=d["url"],
            id=d["id"],
            node_id=d["node_id"],
            html_url=d["html_url"],
            diff_url=d["diff_url"],
            patch_url=d["patch_url"],
            issue_url=d["issue_url"],
            number=d["number"],
            state=d["state"],
            locked=d["locked"],
            title=d["title"],
            user=GitHubUser.from_dict(d["user"]),
            body=d.get("body"),
            created_at=d["created_at"],
            updated_at=d["updated_at"],
            closed_at=d.get("closed_at"),
            merged_at=d.get("merged_at"),
            merge_commit_sha=d.get("merge_commit_sha"),
            assignee=None,
            assignees=d["assignees"],
            requested_reviewers=d["requested_reviewers"],
            requested_teams=d["requested_teams"],
            labels=d["labels"],
            milestone=None,
            draft=d["draft"],
            commits_url=d["commits_url"],
            review_comments_url=d["review_comments_url"],
            review_comment_url=d["review_comment_url"],
            comments_url=d["comments_url"],
            statuses_url=d["statuses_url"],
            author_association=d["author_association"],
            auto_merge=None,
            active_lock_reason=d.get("active_lock_reason"),
            merged=d["merged"],
            mergeable=d.get("mergeable"),
            rebaseable=d.get("rebaseable"),
            mergeable_state=d["mergeable_state"],
            merged_by=GitHubUser.from_dict(d["merged_by"])
            if d.get("merged_by")
            else None,
            comments=d["comments"],
            review_comments=d["review_comments"],
            maintainer_can_modify=d["maintainer_can_modify"],
            commits=d["commits"],
            additions=d["additions"],
            deletions=d["deletions"],
            changed_files=d["changed_files"],
        )
