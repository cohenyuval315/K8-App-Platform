# Define the network name
NETWORK_NAME="frontend-dev-network"

# Check if the network already exists
if ! docker network ls --format '{{.Name}}' | grep -w $NETWORK_NAME > /dev/null; then
  # Create the network if it doesn't exist
  echo "Network '$NETWORK_NAME' does not exist. Creating it..."
  docker network create $NETWORK_NAME
else
  echo "Network '$NETWORK_NAME' already exists."
fi


NETWORK_NAME="backend-dev-network"

# Check if the network already exists
if ! docker network ls --format '{{.Name}}' | grep -w $NETWORK_NAME > /dev/null; then
  # Create the network if it doesn't exist
  echo "Network '$NETWORK_NAME' does not exist. Creating it..."
  docker network create $NETWORK_NAME
else
  echo "Network '$NETWORK_NAME' already exists."
fi
