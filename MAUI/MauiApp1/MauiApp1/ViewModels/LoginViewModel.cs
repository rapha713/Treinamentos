using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

namespace MauiApp1.ViewModels;

public class LoginViewModel : INotifyPropertyChanged
{
    public event PropertyChangedEventHandler PropertyChanged;

    void OnPropertyChanged([CallerMemberName] string name = null)
        => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));

    private string user;
    public string User
    {
        get => user;
        set
        {
            user = value;
            OnPropertyChanged();
        }
    }

    private string password;
    public string Password
    {
        get => password;
        set
        {
            password = value;
            OnPropertyChanged();
        }
    }

    public ICommand LoginCommand { get; }

    public LoginViewModel()
    {
        LoginCommand = new Command(async () => await Login());
    }

    private async Task Login()
    {
        if (string.IsNullOrWhiteSpace(User) || string.IsNullOrWhiteSpace(Password))
        {
            await Application.Current.MainPage.DisplayAlertAsync("Erro", "Preencha tudo", "OK");
            return;
        }

        await Task.Delay(2000);

        if (User == "admin" && Password == "123")
            await Application.Current.MainPage.DisplayAlertAsync("Sucesso", "Login OK", "OK");
        else
            await Application.Current.MainPage.DisplayAlertAsync("Erro", "Inválido", "OK");
    }
}