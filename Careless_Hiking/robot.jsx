import React, { useState } from "react";

const RobotApp = () => {
  const [token, setToken] = useState("");
  const [output, setOutput] = useState("Aquí aparecerá la respuesta...");

  // Datos fijos
  const URL_ENDPOINT = "https://es.robotkeenon.com/api/open/scene/v1/robot/call/task";
  const STORE_ID = "C00001185";

  // Endpoints: uuid y pointId por botón
  const endpoints = [
    { name: "Uredi", uuid: "bcba6e7206707ef0d79bb5d467ab40ea", pointId: "4" },
    { name: "Stolovi", uuid: "a09184ff12e5f5122069263507956287", pointId: "5" },
    { name: "Devs", uuid: "cb31d7e7f1d724726d65c972e9739706", pointId: "15" },
    { name: "New guys", uuid: "f30e8650b6c6799d260cfc36d9a63765", pointId: "16" },
  ];

  // Función para actualizar token
  const updateToken = async () => {
    setOutput("Obteniendo token...");
    try {
      const res = await fetch("https://es.robotkeenon.com/api/open/oauth/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({
          client_id: "MFPPuu0GtJUIDpwX",
          client_secret: "XRxN2SV2RPJfWW3n",
          grant_type: "client_credentials",
        }),
      });

      if (!res.ok) throw new Error("HTTP error " + res.status);
      const data = await res.json();
      setToken(data.access_token);
      setOutput("Token actualizado: " + data.access_token);
    } catch (err) {
      setOutput("Error al obtener token: " + err.message);
    }
  };

  // Función para enviar datos de cada botón
  const fetchData = async (index) => {
    if (!token) {
      setOutput("Primero actualiza el token");
      return;
    }

    const ep = endpoints[index];
    const formData = new FormData();
    formData.append("uuid", ep.uuid);
    formData.append("pointId", ep.pointId);
    formData.append("storeId", STORE_ID);

    setOutput(`Cargando ${ep.name}...`);

    try {
      const res = await fetch(URL_ENDPOINT, {
        method: "POST",
        headers: { Authorization: "Bearer " + token },
        body: formData,
      });

      if (!res.ok) throw new Error("HTTP error " + res.status);
      const data = await res.json();
      setOutput(JSON.stringify(data, null, 2));
    } catch (err) {
      setOutput(`Error en ${ep.name}: ${err.message}`);
    }
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: 20, textAlign: "center", background: "#f5f5f5" }}>
      <div style={{ display: "flex", justifyContent: "flex-start", marginBottom: 20 }}>
        <button
          onClick={updateToken}
          style={{ padding: 10, borderRadius: 10, background: "#d3aaff", color: "white", border: "none", cursor: "pointer" }}
        >
          Actualizar Token
        </button>
      </div>

      <h1>Robot</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 10,
          maxWidth: 600,
          margin: "0 auto 20px auto",
        }}
      >
        {endpoints.map((ep, index) => (
          <button
            key={index}
            onClick={() => fetchData(index)}
            style={{ padding: 10, borderRadius: 10, background: "#d3aaff", color: "white", border: "none", cursor: "pointer" }}
          >
            {ep.name}
          </button>
        ))}
      </div>

      <pre
        style={{
          background: "white",
          padding: 15,
          borderRadius: 10,
          maxHeight: 300,
          overflow: "auto",
          textAlign: "left",
          maxWidth: 600,
          margin: "0 auto",
        }}
      >
        {output}
      </pre>

      <img
        src="sticker-removebg-preview.png"
        alt="Sticker"
        style={{ marginTop: 20, maxWidth: 200 }}
      />
    </div>
  );
};

export default RobotApp;