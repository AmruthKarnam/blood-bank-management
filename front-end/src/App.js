import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
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
import ListDonorAnalysis from './usr/analyst/ListDonorAnalysis';
import HospitalRequests from './usr/manager/HospitalRequests';

function App() {
  const [userInfo, setUserInfo] = useState({ userName: "", userPassword: "", userType: "" });
  const navigate = useNavigate();

  const handleLogin = (info) => {
    setUserInfo(info);
    console.log("HEREEEEEE");
    console.log(info);
    if (info.userType === 'analyst') {
      navigate('/analyst', { state: { userInfo: info } });
    } else if (info.userType === 'manager') {
      navigate('/manager', { state: { userInfo: info } });
    } else if (info.userType === 'admin') {
      navigate('/admin', { state: { userInfo: info } });
    } 
  };
  return (
      <div className="App">
      <h1>APPPPPP/</h1>
        <Routes>
          <Route path="/" element={<Login setUserInfo = {handleLogin} />} />
          <Route path="/manager" element={<ManagerDashboard />} />
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/analyst" element={<AnalystDashboard/>} />
          <Route path="/manager/BloodUnitModifications" element={<BloodUnitModifications />} />
          <Route path="/manager/BloodRequests" element={<BloodRequests />} />
          <Route path="/manager/AdminModifications" element={<AdminModifications />} />
          <Route path="/manager/AnalystModifications" element={<AnalystModifications />} />
          <Route path="/manager/HospitalRequests" element={<HospitalRequests />} />
          <Route path="/admin/PatientRegistration" element={<PatientRegistration userInfo ={userInfo}/>} />
          <Route path="/admin/DonorRegistration" element={<DonorRegistration userInfo ={userInfo}/>} />
          <Route path="/analyst/AddDonorAnalysis" element={<AddDonorAnalysis />} />
          <Route path="/analyst/ListDonorAnalysis" element={<ListDonorAnalysis />} />
          <Route path="/analyst/ListDonorsToAnalyse" element={<ListDonorsToAnalyse userInfo ={userInfo}/>} />
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
  );
}

export default App;