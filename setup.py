"""Entry point for setuptools, configuration is in setup.cfg."""

import re
from pathlib import Path
from typing import List

from semver.version import Version
from setuptools import setup

ROOT_DIR = Path(__file__).parent
SEMVER_RE = re.compile(r"(?:#{2}\s*\[)(?P<version>.*)(?:\])")


def semver_from(changelog: Path) -> Version:
    """Retrieve latest Semantic Version (SemVer) from ``changelog``."""
    with open(changelog) as f:
        matches = SEMVER_RE.finditer(f.read())
        versions: List[Version] = []
        is_unreleased = False
        for match in matches:
            version = match.groupdict()["version"]
            if version.lower() == "unreleased":
                is_unreleased = True
            else:
                versions.append(Version.parse(version))

        versions.sort()
        latest = versions[-1]
        print(latest)
        return latest.bump_prerelease() if is_unreleased else latest


if __name__ == "__main__":
    setup(
        use_scm_version={
            "fallback_version": semver_from(ROOT_DIR / "CHANGELOG.md"),
        }
    )
