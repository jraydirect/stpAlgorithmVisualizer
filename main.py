import turtle
import math


# Constants
NODE_RADIUS = 10  # Radius of the nodes
NODE_DISTANCE = 150  # Distance between nodes
EDGE_COLOR = "black"
NODE_COLOR = "blue"
TEXT_COLOR = "black"
DRAW_SPEED = 3  # Speed of the drawing animation

# Function to draw a node
def draw_node(turtle, x, y, label):
    turtle.penup()
    turtle.goto(x, y - NODE_RADIUS)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(NODE_RADIUS)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y - NODE_RADIUS - 20)
    turtle.write(label, align="center", font=("Arial", 10, "normal"))

# Function to draw an edge between two nodes
def draw_edge(turtle, x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1 - NODE_RADIUS)
    turtle.pendown()
    turtle.goto(x2, y2 - NODE_RADIUS)

# Function to draw an edge between two nodes with animation
def draw_edge_with_animation(turtle, x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1 - NODE_RADIUS)
    turtle.pendown()
    turtle.speed(DRAW_SPEED)  # Set the speed for animation
    turtle.goto(x2, y2 - NODE_RADIUS)


# Function to draw the spanning tree resulting from RSTP with animation
def draw_rstp_spanning_tree_with_animation(num_nodes):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen
    screen.bgcolor("white")

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the maximum
    t.color(EDGE_COLOR)

    # Draw nodes evenly spaced in a circle
    node_positions = []
    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = 0 + NODE_DISTANCE * math.cos(angle)
        y = 0 + NODE_DISTANCE * math.sin(angle)
        draw_node(t, x, y, str(i))
        node_positions.append((x, y))

    # Draw edges between nodes to represent the spanning tree with animation
    for i in range(1, num_nodes):
        draw_edge_with_animation(t, node_positions[i][0], node_positions[i][1],
                                 node_positions[i-1][0], node_positions[i-1][1])

    # Draw edge from last node to first node to complete the cycle with animation
    draw_edge_with_animation(t, node_positions[num_nodes - 1][0], node_positions[num_nodes - 1][1],
                             node_positions[0][0], node_positions[0][1])

    # Add text to explain what's going on
    text_turtle = turtle.Turtle()
    text_turtle.penup()
    text_turtle.color(TEXT_COLOR)
    text_turtle.goto(0, 250)
    text_turtle.write("RSTP Spanning Tree", align="center", font=("Arial", 16, "bold"))
    text_turtle.goto(0, 200)
    text_turtle.write("Enhances STP by reducing convergence times through the elimination of listening and learning states and the introduction of port roles and types.", align="center", font=("Arial", 12, "normal"))

    # Hide turtles
    t.hideturtle()
    text_turtle.hideturtle()

    # Keep the window open
    turtle.done()

# Function to draw the spanning tree resulting from MSTP with animation
def draw_mstp_spanning_tree_with_animation(num_nodes):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen
    screen.bgcolor("white")

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the maximum
    t.color(EDGE_COLOR)

    # Draw nodes evenly spaced in a circle
    node_positions = []
    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = 0 + NODE_DISTANCE * math.cos(angle)
        y = 0 + NODE_DISTANCE * math.sin(angle)
        draw_node(t, x, y, str(i))
        node_positions.append((x, y))

    # Draw edges between nodes to represent the spanning tree with animation
    for i in range(1, num_nodes):
        draw_edge_with_animation(t, node_positions[i][0], node_positions[i][1],
                                 node_positions[0][0], node_positions[0][1])

    # Add text to explain what's going on
    text_turtle = turtle.Turtle()
    text_turtle.penup()
    text_turtle.color(TEXT_COLOR)
    text_turtle.goto(0, 250)
    text_turtle.write("MSTP Spanning Tree", align="center", font=("Arial", 16, "bold"))
    text_turtle.goto(0, 200)
    text_turtle.write("Extends RSTP to support multiple VLANs, optimizing network resource utilization by creating multiple spanning trees.", align="center", font=("Arial", 12, "normal"))

    # Hide turtles
    t.hideturtle()
    text_turtle.hideturtle()

    # Keep the window open
    turtle.done()


# Function to draw the spanning tree resulting from PVSTP with animation
def draw_pvstp_spanning_tree_with_animation(num_nodes):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen
    screen.bgcolor("white")

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the maximum
    t.color(EDGE_COLOR)

    # Draw nodes evenly spaced in a circle
    node_positions = []
    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = 0 + NODE_DISTANCE * math.cos(angle)
        y = 0 + NODE_DISTANCE * math.sin(angle)
        draw_node(t, x, y, str(i))
        node_positions.append((x, y))

    # Draw edges between nodes to represent the spanning tree with animation
    for i in range(1, num_nodes):
        draw_edge_with_animation(t, node_positions[i][0], node_positions[i][1],
                                 node_positions[0][0], node_positions[0][1])

    # Add text to explain what's going on
    text_turtle = turtle.Turtle()
    text_turtle.penup()
    text_turtle.color(TEXT_COLOR)
    text_turtle.goto(0, 250)
    text_turtle.write("PVSTP Spanning Tree", align="center", font=("Arial", 16, "bold"))
    text_turtle.goto(0, 200)
    text_turtle.write("Cisco's proprietary extension of STP, creating separate spanning tree instances for each VLAN to provide redundancy and load balancing.", align="center", font=("Arial", 12, "normal"))

    # Hide turtles
    t.hideturtle()
    text_turtle.hideturtle()

    # Keep the window open
    turtle.done()

# Function to draw the spanning tree resulting from SPB with animation
def draw_spb_spanning_tree_with_animation(num_nodes):
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Fullscreen
    screen.bgcolor("white")

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the drawing speed to the maximum
    t.color(EDGE_COLOR)

    # Draw nodes in a grid
    node_positions = []
    rows = int(math.sqrt(num_nodes))
    cols = num_nodes // rows
    for i in range(rows):
        for j in range(cols):
            x = (j - cols // 2) * NODE_DISTANCE
            y = (i - rows // 2) * NODE_DISTANCE
            draw_node(t, x, y, f"{i*cols + j}")
            node_positions.append((x, y))

    # Draw edges between adjacent nodes in the grid with animation
    for i in range(len(node_positions)):
        for j in range(i + 1, len(node_positions)):
            if abs(i - j) == 1 or abs(i - j) == cols:
                draw_edge_with_animation(t, node_positions[i][0], node_positions[i][1],
                                         node_positions[j][0], node_positions[j][1])
    
    # Add text to explain what's going on
    text_turtle = turtle.Turtle()
    text_turtle.penup()
    text_turtle.color(TEXT_COLOR)
    text_turtle.goto(0, 250)
    text_turtle.write("SPB Spanning Tree", align="center", font=("Arial", 16, "bold"))
    text_turtle.goto(0, 200)
    text_turtle.write(" IEEE 802.1aq enables the creation of multiple equal-cost spanning trees, enhancing scalability and convergence in large networks.", align="center", font=("Arial", 12, "normal"))

    # Hide turtles
    t.hideturtle()
    text_turtle.hideturtle()

    # Keep the window open
    turtle.done()


# Main function
def main():
    # Prompt the user to choose the STP algorithm
    print("Choose an STP algorithm:")
    print("1. Rapid Spanning Tree Protocol (RSTP)")
    print("2. Multiple Spanning Tree Protocol (MSTP)")
    print("3. Per-VLAN Spanning Tree Protocol (PVSTP)")
    print("4. IEEE 802.1aq - Shortest Path Bridging (SPB)")


    choice = input("Enter your choice (1, 2, 3, or 4): ")

    num_nodes = int(input("Enter the number of nodes: "))

    if choice == "1":
        draw_rstp_spanning_tree_with_animation(num_nodes)
    elif choice == "2":
        draw_mstp_spanning_tree_with_animation(num_nodes)
    elif choice == "3":
        draw_pvstp_spanning_tree_with_animation(num_nodes)
    elif choice == "4":
        draw_spb_spanning_tree_with_animation(num_nodes)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
