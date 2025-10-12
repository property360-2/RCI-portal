import { 
  Users, 
  FileText, 
  TrendingUp, 
  CheckCircle,
  Clock,
  UserCheck,
  AlertCircle,
  Download,
  Search,
  Filter
} from 'lucide-react'
import useAuthStore from '../store/useAuthStore'
import DashboardLayout from '../components/layout/DashboardLayout'

const RegistrarDashboard = () => {
  const user = useAuthStore((state) => state.user)

  const stats = [
    { 
      label: 'Total Students', 
      value: '1,234', 
      icon: Users, 
      change: '+48 this month',
      bgGradient: 'from-blue-500 to-blue-600'
    },
    { 
      label: 'Documents Processed', 
      value: '856', 
      icon: FileText, 
      change: '+120 this week',
      bgGradient: 'from-green-500 to-emerald-600'
    },
    { 
      label: 'Pending Requests', 
      value: '23', 
      icon: Clock, 
      change: '5 urgent',
      bgGradient: 'from-orange-500 to-orange-600'
    },
    { 
      label: 'Verified Records', 
      value: '98%', 
      icon: CheckCircle, 
      change: '+2% this month',
      bgGradient: 'from-purple-500 to-purple-600'
    },
  ]

  const recentRequests = [
    { 
      student: 'Juan Dela Cruz', 
      studentId: '2021-00123',
      document: 'Transcript of Records', 
      status: 'pending',
      date: '2025-10-12',
      priority: 'high'
    },
    { 
      student: 'Maria Santos', 
      studentId: '2021-00456',
      document: 'Certificate of Enrollment', 
      status: 'processing',
      date: '2025-10-11',
      priority: 'normal'
    },
    { 
      student: 'Pedro Reyes', 
      studentId: '2021-00789',
      document: 'Diploma', 
      status: 'completed',
      date: '2025-10-10',
      priority: 'normal'
    },
  ]

  const recentActivities = [
    { action: 'Verified student records for BSCS 3-A', time: '5 minutes ago', type: 'verify' },
    { action: 'Generated enrollment report', time: '1 hour ago', type: 'report' },
    { action: 'Processed transcript request', time: '2 hours ago', type: 'document' },
    { action: 'Updated student information', time: '3 hours ago', type: 'update' },
  ]

  const getStatusColor = (status) => {
    if (status === 'completed') return 'bg-green-100 text-green-800 border-green-200'
    if (status === 'processing') return 'bg-blue-100 text-blue-800 border-blue-200'
    if (status === 'pending') return 'bg-orange-100 text-orange-800 border-orange-200'
    return 'bg-gray-100 text-gray-800 border-gray-200'
  }

  const getPriorityBadge = (priority) => {
    if (priority === 'urgent') return 'bg-red-100 text-red-700 border-red-200'
    if (priority === 'high') return 'bg-orange-100 text-orange-700 border-orange-200'
    return 'bg-gray-100 text-gray-700 border-gray-200'
  }

  const getActivityIcon = (type) => {
    if (type === 'verify') return <UserCheck className="w-4 h-4 text-green-600" />
    if (type === 'report') return <FileText className="w-4 h-4 text-blue-600" />
    if (type === 'document') return <Download className="w-4 h-4 text-orange-600" />
    return <AlertCircle className="w-4 h-4 text-gray-600" />
  }

  const getActivityBg = (type) => {
    if (type === 'verify') return 'bg-green-100'
    if (type === 'report') return 'bg-blue-100'
    if (type === 'document') return 'bg-orange-100'
    return 'bg-gray-100'
  }

  return (
    <DashboardLayout>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
        <div className="p-6 max-w-7xl mx-auto">
          <div className="mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-2">
              Welcome back, <span className="text-green-600">{user?.username || 'Registrar'}</span>!
            </h1>
            <p className="text-gray-600 text-lg">Here is your registrar overview for today</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            {stats.map((stat, index) => (
              <div
                key={index}
                className="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden group hover:-translate-y-1"
              >
                <div className={`h-2 bg-gradient-to-r ${stat.bgGradient}`}></div>
                <div className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <div className={`p-3 bg-gradient-to-r ${stat.bgGradient} rounded-xl`}>
                      <stat.icon className="w-6 h-6 text-white" />
                    </div>
                    <span className="text-3xl font-bold text-gray-900">{stat.value}</span>
                  </div>
                  <h3 className="text-sm font-medium text-gray-600 mb-1">{stat.label}</h3>
                  <p className="text-xs text-gray-500">{stat.change}</p>
                </div>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div className="lg:col-span-2 bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                  <FileText className="w-6 h-6 text-green-600" />
                  Recent Document Requests
                </h2>
                <div className="flex gap-2">
                  <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                    <Search className="w-5 h-5 text-gray-600" />
                  </button>
                  <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
                    <Filter className="w-5 h-5 text-gray-600" />
                  </button>
                </div>
              </div>
              
              <div className="space-y-3">
                {recentRequests.map((request, index) => (
                  <div
                    key={index}
                    className="p-4 border border-gray-200 rounded-xl hover:border-green-300 hover:shadow-md transition-all duration-200"
                  >
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <h3 className="font-semibold text-gray-900">{request.student}</h3>
                          <span className="text-xs text-gray-500">({request.studentId})</span>
                          {request.priority !== 'normal' && (
                            <span className={`px-2 py-0.5 text-xs font-semibold rounded border ${getPriorityBadge(request.priority)}`}>
                              {request.priority.toUpperCase()}
                            </span>
                          )}
                        </div>
                        <p className="text-sm text-gray-600 mb-1">{request.document}</p>
                        <p className="text-xs text-gray-500">Requested: {request.date}</p>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className={`px-3 py-1 text-xs font-semibold rounded-full border ${getStatusColor(request.status)}`}>
                          {request.status.charAt(0).toUpperCase() + request.status.slice(1)}
                        </span>
                        <button className="px-4 py-2 text-sm font-medium text-green-600 hover:bg-green-50 rounded-lg transition-colors">
                          View
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

              <button className="w-full mt-4 py-3 text-sm font-medium text-green-600 hover:bg-green-50 rounded-lg transition-colors">
                View All Requests
              </button>
            </div>

            <div className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center gap-2 mb-6">
                <TrendingUp className="w-6 h-6 text-purple-600" />
                <h2 className="text-2xl font-bold text-gray-900">Recent Activity</h2>
              </div>
              
              <div className="space-y-4">
                {recentActivities.map((activity, index) => (
                  <div
                    key={index}
                    className="p-3 border-l-4 border-purple-500 bg-purple-50 rounded-r-lg"
                  >
                    <div className="flex items-start gap-3">
                      <div className={`p-2 rounded-lg ${getActivityBg(activity.type)}`}>
                        {getActivityIcon(activity.type)}
                      </div>
                      <div className="flex-1">
                        <p className="text-sm font-medium text-gray-900 mb-1">
                          {activity.action}
                        </p>
                        <p className="text-xs text-gray-500">{activity.time}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

              <button className="w-full mt-4 py-2 text-sm font-medium text-purple-600 hover:bg-purple-50 rounded-lg transition-colors">
                View All Activity
              </button>
            </div>
          </div>

          <div className="bg-gradient-to-br from-green-600 to-emerald-700 rounded-2xl shadow-lg p-6 text-white">
            <h2 className="text-2xl font-bold mb-6">Quick Actions</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <button className="bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-white/20 rounded-lg">
                    <Users className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Manage Students</h3>
                    <p className="text-sm text-green-100">View and edit records</p>
                  </div>
                </div>
              </button>
              
              <button className="bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-white/20 rounded-lg">
                    <FileText className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Process Documents</h3>
                    <p className="text-sm text-green-100">Handle requests</p>
                  </div>
                </div>
              </button>
              
              <button className="bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-white/20 rounded-lg">
                    <Download className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Generate Reports</h3>
                    <p className="text-sm text-green-100">Export data</p>
                  </div>
                </div>
              </button>
              
              <button className="bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-white/20 rounded-lg">
                    <CheckCircle className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Verify Records</h3>
                    <p className="text-sm text-green-100">Approve changes</p>
                  </div>
                </div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </DashboardLayout>
  )
}

export default RegistrarDashboard