import { useState } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { 
  LogOut, 
  Menu, 
  X, 
  Home, 
  BookOpen, 
  Users, 
  FileText, 
  Settings,
  GraduationCap,
  Bell,
  User,
  ChevronDown
} from 'lucide-react'
import useAuthStore from '../../store/useAuthStore'

const DashboardLayout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [profileMenuOpen, setProfileMenuOpen] = useState(false)
  const { user, clearAuth } = useAuthStore()
  const navigate = useNavigate()
  const location = useLocation()

  const handleLogout = () => {
    clearAuth()
    navigate('/login')
  }

  // Navigation items based on role
  const getNavItems = () => {
    const roleNavItems = {
      student: [
        { name: 'Dashboard', icon: Home, path: '/student/dashboard' },
        { name: 'My Profile', icon: User, path: '/student/profile' },
        { name: 'Enrollment', icon: BookOpen, path: '/student/enrollment' },
        { name: 'My Subjects', icon: BookOpen, path: '/student/subjects' },
        { name: 'Grades', icon: GraduationCap, path: '/student/grades' },
        { name: 'Documents', icon: FileText, path: '/student/documents' },
      ],
      registrar: [
        { name: 'Dashboard', icon: Home, path: '/registrar/dashboard' },
        { name: 'Students', icon: Users, path: '/registrar/students' },
        { name: 'Records', icon: FileText, path: '/registrar/records' },
        { name: 'Documents', icon: FileText, path: '/registrar/documents' },
      ],
      admission: [
        { name: 'Dashboard', icon: Home, path: '/admission/dashboard' },
        { name: 'Applications', icon: FileText, path: '/admission/applications' },
        { name: 'Applicants', icon: Users, path: '/admission/applicants' },
      ],
      head: [
        { name: 'Dashboard', icon: Home, path: '/head/dashboard' },
        { name: 'Professors', icon: Users, path: '/head/professors' },
        { name: 'Subjects', icon: BookOpen, path: '/head/subjects' },
        { name: 'Analytics', icon: Settings, path: '/head/analytics' },
      ],
      professor: [
        { name: 'Dashboard', icon: Home, path: '/professor/dashboard' },
        { name: 'My Classes', icon: BookOpen, path: '/professor/classes' },
        { name: 'Students', icon: Users, path: '/professor/students' },
        { name: 'Grades', icon: GraduationCap, path: '/professor/grades' },
      ],
      admin: [
        { name: 'Dashboard', icon: Home, path: '/admin/dashboard' },
        { name: 'Users', icon: Users, path: '/admin/users' },
        { name: 'Programs', icon: BookOpen, path: '/admin/programs' },
        { name: 'Settings', icon: Settings, path: '/admin/settings' },
      ],
    }

    return roleNavItems[user?.role] || []
  }

  const isActivePath = (path) => location.pathname === path

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar */}
      <aside
        className={`
          fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-blue-600 to-indigo-700 
          transform transition-transform duration-300 ease-in-out
          lg:translate-x-0 lg:static
          ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}
        `}
      >
        <div className="h-full flex flex-col text-white">
          {/* Logo */}
          <div className="p-6 border-b border-white/10">
            <div className="flex items-center gap-3 mb-2">
              <div className="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
                <GraduationCap className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold">Richwell Colleges, Incorporated</h1>
                <p className="text-xs text-blue-200 capitalize">{user?.role || 'User'}</p>
              </div>
            </div>
          </div>

          {/* Navigation */}
          <nav className="flex-1 p-4 space-y-1 overflow-y-auto">
            {getNavItems().map((item) => {
              const isActive = isActivePath(item.path)
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  onClick={() => setSidebarOpen(false)}
                  className={`
                    flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200
                    ${isActive 
                      ? 'bg-white text-blue-600 shadow-lg' 
                      : 'text-blue-100 hover:bg-white/10 hover:text-white'
                    }
                  `}
                >
                  <item.icon className="w-5 h-5" />
                  <span className="font-medium">{item.name}</span>
                  {isActive && (
                    <div className="ml-auto w-2 h-2 bg-blue-600 rounded-full"></div>
                  )}
                </Link>
              )
            })}
          </nav>

          {/* User Section */}
          <div className="p-4 border-t border-white/10">
            <div className="relative">
              <button
                onClick={() => setProfileMenuOpen(!profileMenuOpen)}
                className="w-full flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/10 transition-colors"
              >
                <div className="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
                  <User className="w-5 h-5" />
                </div>
                <div className="flex-1 text-left">
                  <p className="text-sm font-semibold truncate">{user?.username || 'User'}</p>
                  <p className="text-xs text-blue-200 truncate">{user?.email || 'user@rci.edu'}</p>
                </div>
                <ChevronDown className={`w-4 h-4 transition-transform ${profileMenuOpen ? 'rotate-180' : ''}`} />
              </button>

              {profileMenuOpen && (
                <div className="absolute bottom-full left-0 right-0 mb-2 bg-white rounded-xl shadow-xl overflow-hidden">
                  <button
                    onClick={() => {
                      setProfileMenuOpen(false)
                      // Navigate to profile
                    }}
                    className="w-full px-4 py-3 text-left text-gray-700 hover:bg-gray-50 flex items-center gap-3 transition-colors"
                  >
                    <Settings className="w-4 h-4" />
                    <span className="text-sm font-medium">Settings</span>
                  </button>
                  <button
                    onClick={handleLogout}
                    className="w-full px-4 py-3 text-left text-red-600 hover:bg-red-50 flex items-center gap-3 transition-colors"
                  >
                    <LogOut className="w-4 h-4" />
                    <span className="text-sm font-medium">Logout</span>
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col min-h-screen">
        {/* Top Navigation Bar */}
        <header className="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
          <div className="px-6 py-4 flex items-center justify-between">
            <div className="flex items-center gap-4">
              {/* Mobile Menu Button */}
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="lg:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors"
              >
                {sidebarOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
              </button>

              {/* Page Title - Mobile */}
              <div className="lg:hidden">
                <h1 className="text-lg font-bold text-gray-900">RCI Portal</h1>
              </div>
            </div>

            {/* Right Section */}
            <div className="flex items-center gap-4">
              {/* Notifications */}
              <button className="relative p-2 rounded-lg hover:bg-gray-100 transition-colors">
                <Bell className="w-5 h-5 text-gray-600" />
                <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
              </button>

              {/* User Avatar - Desktop */}
              <div className="hidden lg:flex items-center gap-3">
                <div className="text-right">
                  <p className="text-sm font-semibold text-gray-900">{user?.username || 'User'}</p>
                  <p className="text-xs text-gray-500 capitalize">{user?.role || 'Student'}</p>
                </div>
                <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-full flex items-center justify-center">
                  <span className="text-white font-semibold text-sm">
                    {(user?.username || 'U').charAt(0).toUpperCase()}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 overflow-y-auto">
          {children}
        </main>
      </div>

      {/* Overlay for mobile */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}
    </div>
  )
}

export default DashboardLayout