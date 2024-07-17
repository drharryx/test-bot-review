using UnityEngine;
using Photon.Pun;
using Photon.Realtime;

public class GameManager : MonoBehaviourPunCallbacks
{
    [SerializeField]
    private GameObject playButton;

    private void Start()
    {
        // Asegurarse de que el botón esté desactivado al inicio
        playButton.SetActive(false);
    }

    private void Update()
    {
        // Activar el botón de jugar solo si es el cliente maestro y hay 2 jugadores
        if (PhotonNetwork.IsMasterClient && PhotonNetwork.CurrentRoom.PlayerCount == 2)
        {
            playButton.SetActive(true);
        }
        else
        {
            playButton.SetActive(false);
        }
    }

    public void OnClickPlayButton()
    {
        // Verificar si el cliente que hace clic es el maestro
        if (PhotonNetwork.IsMasterClient)
        {
            // Cargar el nivel del juego principal para todos los clientes
            PhotonNetwork.LoadLevel("MainGame");
        }
        else
        {
            Debug.LogWarning("Solo el cliente maestro puede iniciar el juego.");
        }
    }

    // Método opcional para manejar cambios en la sala
    public override void OnRoomPropertiesUpdate(ExitGames.Client.Photon.Hashtable propertiesThatChanged)
    {
        base.OnRoomPropertiesUpdate(propertiesThatChanged);
        // Aquí puedes manejar cambios en las propiedades de la sala si es necesario
    }

    // Método opcional para manejar la desconexión de jugadores
    public override void OnPlayerLeftRoom(Player otherPlayer)
    {
        base.OnPlayerLeftRoom(otherPlayer);
        // Aquí puedes manejar la lógica cuando un jugador abandona la sala
        playButton.SetActive(false);
    }
}
