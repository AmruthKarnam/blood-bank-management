import React, { useState } from 'react';
import Login from './Login';
import DonorRegistration from './DonorRegistration';
import PatientRegistration from './PatientRegistration';
import ListBloodUnits from './ListBloodUnits'; 
import AddBloodUnits from './AddBloodUnits'
import UpdateBloodUnits from './UpdateBloodUnits'
import BloodRequest from './BloodRequest';
import './styles.css'; // Import styles

const backendApi = "http://localhost:5003"

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
          {userType === 'manager' && (
            <>
              <button onClick={() => setTab('View Blood Units')} className="btn-primary">
                ListBloodUnits
              </button>
              <button onClick={() => setTab('Add Blood Units')} className="btn-primary">
                AddBloodUnits
              </button>
              <button onClick={() => setTab('Update Blood Units')} className="btn-primary">
                UpdateBloodUnits
              </button>
              <button onClick={() => setTab('Blood Requests')} className="btn-primary">
                BloodRequest
              </button>
            </>
          )}
          {userType === 'manager' && selectedTab === 'View Blood Units' && <ListBloodUnits />}
          {userType === 'manager' && selectedTab === 'Add Blood Units' && <AddBloodUnits />}
          {userType === 'manager' && selectedTab === 'Update Blood Units' && <UpdateBloodUnits />}
          {userType === 'manager' && selectedTab === 'Blood Requests' && <BloodRequest />}
        </>
      )}
    </div>
  );
}

export default App;
