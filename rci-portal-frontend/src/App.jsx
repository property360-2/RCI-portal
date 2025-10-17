import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import useAuthStore from "./store/useAuthStore";
import ProtectedRoute from "./components/ProtectedRoute";
import LoginPage from "./pages/LoginPage";
import StudentDashboard from "./pages/StudentDashboard";
import StudentSubjects from "./pages/StudentSubjects";
import RegistrarDashboard from "./pages/RegistrarDashboard";
import DashboardLayout from "./components/layout/DashboardLayout";
import RegisterPage from "./pages/RegisterPage";
// Placeholder components for other roles

const AdmissionDashboard = () => (
  <DashboardLayout>
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Admission Dashboard
        </h1>
        <p className="text-gray-600">Coming soon in Phase 4</p>
      </div>
    </div>
  </DashboardLayout>
);

const HeadDashboard = () => (
  <DashboardLayout>
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Head Dashboard
        </h1>
        <p className="text-gray-600">Coming soon in Phase 4</p>
      </div>
    </div>
  </DashboardLayout>
);

const ProfessorDashboard = () => (
  <DashboardLayout>
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Professor Dashboard
        </h1>
        <p className="text-gray-600">Coming soon in Phase 4</p>
      </div>
    </div>
  </DashboardLayout>
);

const AdminDashboard = () => (
  <DashboardLayout>
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">
          Admin Dashboard
        </h1>
        <p className="text-gray-600">Coming soon in Phase 4</p>
      </div>
    </div>
  </DashboardLayout>
);

const UnauthorizedPage = () => (
  <div className="min-h-screen flex items-center justify-center bg-gray-50">
    <div className="text-center">
      <h1 className="text-6xl font-bold text-gray-900 mb-4">403</h1>
      <p className="text-2xl text-gray-600 mb-8">Unauthorized Access</p>
      <p className="text-gray-500 mb-8">
        You do not have permission to access this page.
      </p>
      <a
        href="/"
        className="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        Go back home
      </a>
    </div>
  </div>
);

const NotFoundPage = () => (
  <div className="min-h-screen flex items-center justify-center bg-gray-50">
    <div className="text-center">
      <h1 className="text-6xl font-bold text-gray-900 mb-4">404</h1>
      <p className="text-2xl text-gray-600 mb-8">Page Not Found</p>
      <p className="text-gray-500 mb-8">
        The page you are looking for does not exist.
      </p>
      <a
        href="/"
        className="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        Go back home
      </a>
    </div>
  </div>
);

function App() {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);

  return (
    <BrowserRouter>
      <Routes>
        {/* Public Routes */}
        <Route
          path="/login"
          element={
            isAuthenticated ? (
              <Navigate to="/dashboard" replace />
            ) : (
              <LoginPage />
            )
          }
        />
        <Route
          path="/register"
          element={
            isAuthenticated ? (
              <Navigate to="/dashboard" replace />
            ) : (
              <RegisterPage />
            )
          }
        />
        {/* Protected Routes - Student */}
        <Route
          path="/student/dashboard"
          element={
            <ProtectedRoute allowedRoles={["student"]}>
              <StudentDashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/student/subjects"
          element={
            <ProtectedRoute allowedRoles={["student"]}>
              <StudentSubjects />
            </ProtectedRoute>
          }
        />

        {/* Protected Routes - Registrar */}
        <Route
          path="/registrar/dashboard"
          element={
            <ProtectedRoute allowedRoles={["registrar"]}>
              <RegistrarDashboard />
            </ProtectedRoute>
          }
        />

        {/* Protected Routes - Admission */}
        <Route
          path="/admissions/dashboard"
          element={
            <ProtectedRoute allowedRoles={["admissions"]}>
              <AdmissionDashboard />
            </ProtectedRoute>
          }
        />

        {/* Protected Routes - Head */}
        <Route
          path="/head/dashboard"
          element={
            <ProtectedRoute allowedRoles={["head"]}>
              <HeadDashboard />
            </ProtectedRoute>
          }
        />

        {/* Protected Routes - Professor */}
        <Route
          path="/professor/dashboard"
          element={
            <ProtectedRoute allowedRoles={["professor"]}>
              <ProfessorDashboard />
            </ProtectedRoute>
          }
        />

        {/* Protected Routes - Admin */}
        <Route
          path="/admin/dashboard"
          element={
            <ProtectedRoute allowedRoles={["admin"]}>
              <AdminDashboard />
            </ProtectedRoute>
          }
        />

        {/* Error Routes */}
        <Route path="/unauthorized" element={<UnauthorizedPage />} />

        {/* Default Routes */}
        <Route
          path="/"
          element={
            isAuthenticated ? (
              <Navigate to="/dashboard" replace />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Navigate
                to={`/${useAuthStore.getState().user?.role}/dashboard`}
                replace
              />
            </ProtectedRoute>
          }
        />

        {/* 404 */}
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
