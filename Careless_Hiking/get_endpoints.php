<?php
header('Content-Type: application/json');

$conn = new mysqli("localhost", "root", "", "practicas");

if ($conn->connect_error) {
    die(json_encode(["error" => "Error conexión"]));
}

$result = $conn->query("SELECT name, uuid, pointId FROM endpoints");

$data = [];

while($row = $result->fetch_assoc()) {
    $data[] = $row;
}

echo json_encode($data);

$conn->close();
?>