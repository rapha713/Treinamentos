namespace MauiApp1;

public partial class Login : ContentPage
{
    public Login()
	{
		InitializeComponent();
    }

    private async void OnLoginClicked(object sender, EventArgs e)
    {
        string user = UserEntry.Text;
        string senha = PasswordEntry.Text;
        bool usuarioValido = user == "admin";
        bool senhaValida = senha == "123";

        await LoginButton.ScaleToAsync(0.95, 100);

        if (string.IsNullOrWhiteSpace(user) || string.IsNullOrWhiteSpace(senha))
        {
            await DisplayAlertAsync("Erro", "Preencha todos os campos", "OK");
            UserEntry.BackgroundColor = Colors.Red;
            UserEntry.TextColor = Colors.White;
            PasswordEntry.BackgroundColor = Colors.Red;
            PasswordEntry.TextColor = Colors.White;
            await LoginButton.ScaleToAsync(1, 100);
            return;
        }
        else
        {
            try
            {
                await Loading(1);

                bool sucesso = await FakeLogin(user, senha);

                if (sucesso)
                {
                    await DisplayAlertAsync("Sucesso", $"Login realizado como {user}!", "OK");
                    UserEntry.Text = "";
                    PasswordEntry.Text = "";
                    UserEntry.BackgroundColor = Colors.Transparent;
                    UserEntry.PlaceholderColor = Colors.DarkGray;
                    PasswordEntry.BackgroundColor = Colors.Transparent;
                    PasswordEntry.PlaceholderColor = Colors.DarkGray;
                    await Navigation.PushAsync(new MainPage());
                }
                else
                {
                    if (!usuarioValido)
                    {
                        UserEntry.BackgroundColor = Colors.Red;
                        UserEntry.PlaceholderColor = Colors.White;
                    }
                    else
                    {
                        UserEntry.BackgroundColor = Colors.Transparent;
                        UserEntry.PlaceholderColor = Colors.DarkGray;
                        UserEntry.TextColor = Colors.Black;
                    }

                    if (!senhaValida)
                    {
                        PasswordEntry.BackgroundColor = Colors.Red;
                        PasswordEntry.PlaceholderColor = Colors.White;
                    }
                    else
                    {
                        PasswordEntry.BackgroundColor = Colors.Transparent;
                        PasswordEntry.PlaceholderColor = Colors.DarkGray;
                        PasswordEntry.TextColor = Colors.Black;
                    }

                    await DisplayAlertAsync("Erro", "Credenciais inválidas", "OK");
                    await LoginButton.ScaleToAsync(1, 100);
                }
            }
            finally
            {
                await LoginButton.ScaleToAsync(1, 100);
                await Loading(2);
            }
        }
    }

    //CLICAR PARA APARECER
    private bool isPasswordVisible = false;

    private async void OnTogglePasswordClicked(object sender, EventArgs e)
    {
        isPasswordVisible = !isPasswordVisible;

        PasswordEntry.IsPassword = !isPasswordVisible;

        TogglePasswordButton.Source = isPasswordVisible
            ? "eyen.png"
            : "eye.png";

        await TogglePasswordButton.ScaleToAsync(0.8, 100);
        await TogglePasswordButton.ScaleToAsync(1, 100);
    }

    //SEGURAR PARA APARECER
    //private void OnPressed(object sender, EventArgs e)
    //{
    //    PasswordEntry.IsPassword = false;
    //    EyeIcon.Source = "eyen.png";
    //    EyeContainer.Scale = 0.8;
    //}

    //private void OnReleased(object sender, EventArgs e)
    //{
    //    PasswordEntry.IsPassword = true;
    //    EyeIcon.Source = "eye.png";
    //    EyeContainer.Scale = 1;
    //}

    //private void OnHoverEnter(object sender, EventArgs e)
    //{
    //    EyeContainer.BackgroundColor = Colors.Azure;
    //}

    //private void OnHoverExit(object sender, EventArgs e)
    //{
    //    EyeContainer.BackgroundColor = Colors.Transparent;
    //}

    async Task<bool> FakeLogin(string user, string senha)
    {
        await Task.Delay(2000);

        return user == "admin" && senha == "123";
    }

    async Task Loading(int n)
    {
        if (n == 1)
        {
            LoadingIndicator.IsRunning = true;
            LoadingIndicator.IsVisible = true;
            LoginButton.IsEnabled = false;
        }
        else
        {
            LoadingIndicator.IsRunning = false;
            LoadingIndicator.IsVisible = false;
            LoginButton.IsEnabled = true;
        }
    }
}