namespace MauiApp1
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private async void OnClicked(object? sender, EventArgs e)
        {
            await Navigation.PushAsync(new Login());
        }
    }
}
