import { Navigate } from 'react-router-dom'
import useAuthStore from '../store/useAuthStore'

/**
 * Protected Route Component
 * Redirects to login if user is not authenticated
 * Optionally checks for specific roles
 */
const ProtectedRoute = ({ children, allowedRoles = [] }) => {
  const { isAuthenticated, user } = useAuthStore()

  // Check if user is authenticated
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }

  // Check if user has required role
  if (allowedRoles.length > 0 && !allowedRoles.includes(user?.role)) {
    return <Navigate to="/unauthorized" replace />
  }

  return children
}

export default ProtectedRoute