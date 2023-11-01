import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import Login from './usr/Login';
import ManagerDashboard from './usr/manager/ManagerDashboard';
import AdminDashboard from './usr/admin/AdminDashboard';
import ListBloodUnits from './usr/manager/ListBloodUnits';
import BloodRequests from './usr/manager/BloodRequest';
import UpdateBloodUnitStatus from './usr/manager/UpdateBloodUnits';
import AddBloodUnits from './usr/manager/AddBloodUnits';
import PatientRegistration from './usr/admin/PatientRegistration';
import DonorRegistration from './usr/admin/DonorRegistration';
import BloodUnitModifications from './usr/manager/BloodUnitModifications'
import AddAdmins from './usr/manager/AddAdmins';
import RemoveAdmins from './usr/manager/RemoveAdmins';
import UpdateAdmins from './usr/manager/UpdateAdmins';
import ListAdmins from './usr/manager/ListAdmins';
import AdminModifications from './usr/manager/AdminModification';
import AnalystModifications from './usr/manager/AnalystModifications'
import AddAnalyst from './usr/manager/AddAnalyst';
import RemoveAnalyst from './usr/manager/RemoveAnalyst';
import ListAnalyst from './usr/manager/ListAnalyst'
import UpdateAnalyst from './usr/manager/UpdateAnalyst';
import AnalystDashboard from './usr/analyst/AnalystDashboard'
import AddDonorAnalysis from './usr/analyst/AddDonorAnalysis';
import ListDonorsToAnalyse from './usr/analyst/ListDonorsToAnalyse';
import ListDonorAnalysis from './usr/analyst/ListDonorAnalysis'

function App() {
  const [userType, setUserType] = useState(null);
  const [adminInfo, setAdminInfo] = useState(null);

  const handleLogin = (type) => {
    setUserType(type);

    // Redirect based on user type
    if (type === 'admin') {
      window.location.href = '/admin';
    } else if (type === 'manager') {
      window.location.href = '/manager';
    } else if (type === 'analyst') {
      window.location.href = '/analyst'
    }
  };
  return (
    <Router>
      <div className="App">
      <h1>APPPPPP/</h1>
        <Routes>
          <Route path="/" element={<Login setUserType={handleLogin} setAdminInfo={setAdminInfo}/>} />
          <Route path="/manager" element={<ManagerDashboard />} />
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/analyst" element={<AnalystDashboard />} />
          <Route path="/manager/BloodUnitModifications" element={<BloodUnitModifications />} />
          <Route path="/manager/BloodRequests" element={<BloodRequests />} />
          <Route path="/manager/AdminModifications" element={<AdminModifications />} />
          <Route path="/manager/AnalystModifications" element={<AnalystModifications />} />
          <Route path="/admin/PatientRegistration" element={<PatientRegistration />} />
          <Route path="/admin/DonorRegistration" element={<DonorRegistration />} />
          <Route path="/analyst/AddDonorAnalysis" element={<AddDonorAnalysis />} />
          <Route path="/analyst/ListDonorAnalysis" element={<ListDonorAnalysis />} />
          <Route path="/analyst/ListDonorsToAnalyse" element={<ListDonorsToAnalyse />} />
          <Route path="/manager/BloodUnitModifications/ListBloodUnits" element={<ListBloodUnits />} />
          <Route path="/manager/BloodUnitModifications/UpdateBloodUnitStatus" element={<UpdateBloodUnitStatus />} />
          <Route path="/manager/BloodUnitModifications/AddBloodUnits" element={<AddBloodUnits />} />
          <Route path="/manager/AdminModifications/ListAdmins" element={<ListAdmins />} />
          <Route path="/manager/AdminModifications/UpdateAdmins" element={<UpdateAdmins />} />
          <Route path="/manager/AdminModifications/RemoveAdmins" element={<RemoveAdmins />} />
          <Route path="/manager/AdminModifications/AddAdmins" element={<AddAdmins />} />
          <Route path="/manager/AnalystModifications/ListAnalyst" element={<ListAnalyst />} />
          <Route path="/manager/AnalystModifications/UpdateAnalyst" element={<UpdateAnalyst />} />
          <Route path="/manager/AnalystModifications/RemoveAnalyst" element={<RemoveAnalyst />} />
          <Route path="/manager/AnalystModifications/AddAnalyst" element={<AddAnalyst />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
