import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import DashboardLayout from './components/Layout/DashboardLayout';
import Home from './components/Dashboard/Home';
import JobSearch from './components/Dashboard/JobSearch';
import ResumeMaker from './components/Dashboard/ResumeMaker';
import CompanyResearch from './components/Dashboard/CompanyResearch';
import MyApplications from './components/Dashboard/MyApplications';
import Profile from './components/Dashboard/Profile';
import './App.css';

const PrivateRoute = ({ children }) => {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" />;
};

function AppContent() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dashboard" element={
        <PrivateRoute>
          <DashboardLayout />
        </PrivateRoute>
      }>
        <Route index element={<Home />} />
        <Route path="jobs" element={<JobSearch />} />
        <Route path="resume" element={<ResumeMaker />} />
        <Route path="companies" element={<CompanyResearch />} />
        <Route path="applications" element={<MyApplications />} />
        <Route path="profile" element={<Profile />} />
      </Route>
      <Route path="/" element={<Navigate to="/dashboard" />} />
    </Routes>
  );
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;