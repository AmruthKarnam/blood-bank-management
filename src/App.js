import React, { useState } from 'react';
import Login from './Login';
import DonorRegistration from './DonorRegistration';
import PatientRegistration from './PatientRegistration';
import './styles.css'; // Import styles

function App() {
  const [userType, setUserType] = useState(null);
  const [selectedTab, setSelectedTab] = useState(null);

  const setTab = (tab) => {
    setSelectedTab(tab);
  };

  return (
    <div className="App">
      {!userType ? (
        <Login setUserType={setUserType} />
      ) : (
        <>
          <h1>Blood Bank Management System</h1>
          {userType === 'admin' && (
            <>
              <button onClick={() => setTab('donor')} className="btn-primary">
                Donor Registration
              </button>
              <button onClick={() => setTab('patient')} className="btn-primary">
                Patient Registration
              </button>
            </>
          )}
          {userType === 'admin' && selectedTab === 'donor' && <DonorRegistration />}
          {userType === 'admin' && selectedTab === 'patient' && <PatientRegistration />}
        </>
      )}
    </div>
  );
}

export default App;
