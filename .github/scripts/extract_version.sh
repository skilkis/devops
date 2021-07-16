# Extract version tag from a release or hotfix branch name 
# MAKE SURE TO RUN git update-index --chmod=+x {path}/extract_version.sh

if [[ $1 =~ (release|hotfix)\/([0-9]\.[0-9]\.[0-9].*) ]]; then
    version=${BASH_REMATCH[2]}
    echo $version
    exit 0
else
    echo "Unable to extract version from branch name $1"
    echo "Ensure branch name is formatted as {hotfix|release}/X.Y.Z"
    exit 1
fi
