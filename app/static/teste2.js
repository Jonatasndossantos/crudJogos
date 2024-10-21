// Inicialize o Firebase
// Substitua com suas configurações
firebase.initializeApp({
  // ...
});

const db = firebase.database();
const dadosContainer = document.getElementById('dados-container');

db.ref('seus-dados').on('value', (snapshot) => {
  dadosContainer.innerHTML = ''; // Limpa o container

  snapshot.forEach((childSnapshot) => {
    const dado = childSnapshot.val();
    // Crie elementos HTML para exibir os dados
    const div = document.createElement('div');
    div.innerHTML = `
      <h2>${dado.titulo}</h2>
      <p>${dado.descricao}</p>
    `;
    dadosContainer.appendChild(div);
  });
});