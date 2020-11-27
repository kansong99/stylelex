

function App() {
      return (
        <div>
          <meta charSet="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>{'{'}{'{'} title {'}'}{'}'} - My Flask App</title>
          <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
          <link rel="stylesheet" type="text/css" href="/static/content/jquery.highlight-within-textarea.css" />
          <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
          <div className="navbar navbar-inverse navbar-fixed-top">
            <div className="container">
              <div className="navbar-header">
                <button type="button" className="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                  <span className="icon-bar" />
                  <span className="icon-bar" />
                  <span className="icon-bar" />
                  <span className="icon-bar" />
                </button>
                <a href="/" className="navbar-brand">StyleLex</a>
              </div>
              <div className="navbar-collapse collapse">
                <ul className="nav navbar-nav">
                  <li><a href="{{ url_for('home') }}">Home</a></li>
                  <li><a href="{{ url_for('product') }}">Product</a></li>
                  <li><a href="{{ url_for('about') }}">About</a></li>
                  <li><a href="{{ url_for('contact') }}">Contact</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div className="container body-content">
            <br />
            {'{'}% block content %{'}'}{'{'}% endblock %{'}'}
          </div>
          {'{'}% block scripts %{'}'}{'{'}% endblock %{'}'}
        </div>
      );
}

  ReactDOM.render(
      <App />,
      document.getElementById('root')
  );