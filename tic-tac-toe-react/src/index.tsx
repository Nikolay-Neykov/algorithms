import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import Game from './game/game.js';
import Home from './home';
import Ranking from './ranking/ranking';
import MainLayout from './main-layout';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <MainLayout>
        <Route path="/home" component={Home} />
        <Route path="/game" component={Game} />
        <Route path="/ranking" component={Ranking} />
        <Route path="*" render={() => <Redirect to="/home" />} />
      </MainLayout>
    </Router>
  );
}

render(<App />, document.getElementById('root'));
